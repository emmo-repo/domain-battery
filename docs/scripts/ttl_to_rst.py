import sys
from rdflib import Graph
import os

########## LOAD TTL ################

def load_ttl_from_file(filepath: str) -> Graph:
    """Loads a Turtle (.ttl) file into an RDFLib Graph."""
    g = Graph()
    g.parse(filepath, format="turtle")
    return g

########## QUERY TTL ################

def extract_terms_info_sparql(g: Graph) -> list:
    text_entities = []

    PREFIXES = """
        PREFIX emmo: <https://w3id.org/emmo#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        """

    list_entity_types = ["IRI", "prefLabel", "Elucidation", "Alternative Label(s)", "IEC Reference", "IUPAC Reference", "Wikipedia Reference", "Wikidata Reference", "Comment"]

    query = PREFIXES + """
        SELECT ?iri ?prefLabel ?elucidation (GROUP_CONCAT(?altLabel; SEPARATOR=", ") AS ?altLabels) ?iecref ?iupacref ?wikipediaref ?wikidataref ?comment
        WHERE {
            ?iri skos:prefLabel ?prefLabel.
            OPTIONAL { ?iri emmo:EMMO_967080e5_2f42_4eb2_a3a9_c58143e835f9 ?elucidation . }
            OPTIONAL { ?iri skos:altLabel ?altLabel . }
            OPTIONAL { ?iri emmo:EMMO_50c298c2_55a2_4068_b3ac_4e948c33181f ?iecref . }
            OPTIONAL { ?iri emmo:EMMO_fe015383_afb3_44a6_ae86_043628697aa2 ?iupacref . }
            OPTIONAL { ?iri emmo:EMMO_c84c6752_6d64_48cc_9500_e54a3c34898d ?wikipediaref . }
            OPTIONAL { ?iri emmo:EMMO_26bf1bef_d192_4da6_b0eb_d2209698fb54 ?wikidataref . }
            OPTIONAL { ?iri rdfs:comment ?comment . }
        }
        GROUP BY ?iri ?prefLabel ?elucidation
        """
        
    qres = g.query(query)

    for hit in qres:    
        hit_dict = {entity_type: str(entity) for entity_type, entity in zip(list_entity_types, hit)}
        text_entities.append(hit_dict)

    text_entities.sort(key=lambda e: e["prefLabel"])
    return text_entities

########## RENDER RST ################

def render_rst_top() -> str:
    return """
===========
Class Index
===========

"""

def entities_to_rst(entities: list[dict]) -> str:
    rst = ""

    for item in entities:
        if '#' not in item['IRI']:
            print(f"Skipping IRI without '#': {item['IRI']}")
            continue  # Skip this entity if no hash is present

        iri_prefix, iri_suffix = item['IRI'].split("#")

        rst += ".. raw:: html\n\n"
        rst += "   <div id=\"" + iri_suffix + "\"></div>\n\n"
        
        rst += item['prefLabel'] + "\n"
        rst += "-" * len(item['prefLabel']) + "\n\n"
        rst += "* " + item['IRI'] + "\n\n"

        rst += ".. raw:: html\n\n"
        indent = "  "
        rst += indent + "<table class=\"element-table\">\n"
        
        for key, value in item.items():
            if key not in ['IRI', 'prefLabel'] and value not in ["None", ""]:
                rst += indent + "<tr>\n"
                rst += indent + "<td class=\"element-table-key\"><span class=\"element-table-key\">" + key + "</span></td>\n"
                
                if value.startswith("http"):
                    value = f"""<a href='{value}'>{value}</a>"""
                else:
                    value = value.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    value = value.replace('\n', '\n' + indent)

                rst += indent + "<td class=\"element-table-value\">" + value + "</td>\n"
                rst += indent + "</tr>\n"
        
        rst += indent + "</table>\n\n"

    return rst

def render_rst_bottom() -> str:
    return "\n"

########### RUN THE RENDERING WORKFLOW ##############

def rendering_workflow(ttl_list_file: str):
    """Reads TTL file paths from list and processes them."""
    
    # Read file paths from the list
    with open(ttl_list_file, "r") as f:
        ttl_files = [line.strip() for line in f.readlines()]

    if not ttl_files:
        raise FileNotFoundError("No valid TTL files found.")

    rst_filename = "battery.rst"
    rst = render_rst_top()

    for ttl_file in ttl_files:
        print(f"Processing: {ttl_file}")
        g = load_ttl_from_file(ttl_file)
        entities_list = extract_terms_info_sparql(g)
        
        page_title = os.path.basename(ttl_file).replace(".ttl", "").capitalize()
        rst += page_title + "\n"
        rst += "=" * len(page_title) + "\n\n"
        rst += entities_to_rst(entities_list)

    rst += render_rst_bottom()

    os.makedirs("./docs", exist_ok=True)
    with open("./docs/" + rst_filename, "w+", encoding="utf-8") as f:
        f.write(rst)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ttl_to_rst.py ttl_files_list.txt")
        sys.exit(1)

    ttl_list_file = sys.argv[1]
    rendering_workflow(ttl_list_file)
