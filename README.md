[![DOI](https://zenodo.org/badge/570454101.svg)](https://zenodo.org/badge/latestdoi/570454101)
![docs](https://github.com/emmo-repo/domain-battery/actions/workflows/doc.yml/badge.svg)


<!-- markdownlint-disable MD033 -->

# Battery Domain Ontology

<!-- [![CI tests](https://github.com/emmo-repo/domain-battery/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-battery/actions/) -->

The Battery Domain Ontology is a specialized domain within the Elementary Multiperspective Materials Ontology [(EMMO)][1], that encompasses essential terms and relationships for battery systems, materials, methods, and data. Its primary objective is to enable the creation of linked and FAIR (Findable, Accessible, Interoperable, and Reusable) data, thereby fostering advancements in research and innovation within the realm of battery. This ontology serves as a foundational resource for harmonizing battery knowledge representation, enhancing data interoperability, and accelerating progress in battery research and development.

A reference documentation is available in [html](https://emmo-repo.github.io/domain-battery/index.html).

### Persistent Identifiers

This ontology assigns persistent machine-readable identifiers to concepts from the battery domain. These identifiers facilitate data exchange and interoperability among various tools and systems. It includes annotations to other sources of information including [DBPedia](https://www.dbpedia.org/) and [Wikidata](https://www.wikidata.org/). 

### Standardized Nomenclature

The ontology builds on standardized nomenclature for battery, relying on recognized authorities including [IUPAC](https://iupac.org/what-we-do/nomenclature/) and the [IEC](https://www.electropedia.org/). IUPAC is the universally-recognized authority on chemical nomenclature and terminology, and IEC is the the world's leading organization that prepares and publishes International Standards for all electrical, electronic and related technologies. This consistency in naming conventions enhances collaboration and data sharing.

## Key Features

- Seamless integration with the EMMO ontology.
- Provides persistent machine-readable identifiers for battery systems, devices, methods, datasets, and quantities.
- Standardized nomenclature for battery entities.
- Facilitates data exchange and interoperability within the EMMO ecosystem.

## Usage

Researchers, domain experts, and developers within the battery communities can utilize the ontology for various purposes, including:

- Incorporating consistent and standardized information into their modeling and simulation activities.
- Enhancing data interoperability between modeling tools, databases, and platforms.
- Supporting research projects that require precise and standardized battery knowledge representation.
- Building applications, databases, or knowledge graphs that leverage EMMO and require battery information.
- Generating linked data in the semantic web.
- Complying with FAIR data mandates (FAIR Guidelines available [here](FAIR.md))

## Structure and Integration with EMMO

The Battery Domain Ontology is an official domain on the EMMO. The asserted source consists of two files:
- `battery.ttl`: describes terms and object properties for the battery domain.
- `batteryquantities.ttl`: describes the physical quantities related to the battery domain. It is encapsulated to allow it to be imported by other EMMO domains without needing to import the entire ontology.

The battery domain also imports other EMMO domains:
- [Chemical Substance Domain Ontology](https://github.com/emmo-repo/domain-chemical-substance): provides material annotations for battery (meta)data.

The import structure is summarized in the following table:
| Imported Ontologies | Version           |
| ------------------- | ----------------- |
| EMMO                | 1.0.0-beta5       |
| chemical-substance  | 0.2.0-alpha       |
| electrochemistry    | 0.7.0-alpha       |

For simplicity, we complie the source files and other imports into a [pre-inferred ontology](inferred_version/battery-inferred.ttl). This is the result of running the asserted source files through a semantic reasoner and includes both asserted and inferred properties in a clear graph. 

## Getting Started

### Prerequisites

Before you begin, we recommend that you install the following tools. They are not all required, but greatly simplify the process of working with ontologies:

- [Protégé](https://protege.stanford.edu/) (a graphical ontology editor)
  - Installation instructions are available [here](https://protege.stanford.edu/software.php#desktop-protege).

- [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy) (python package for working with EMMO ontologies)
  - Installation instructions are available [here](https://github.com/emmo-repo/EMMOntoPy#installation).

- [RDFLib](https://rdflib.readthedocs.io/en/stable/) (optional, python package for working with RDF graphs)
  - Installation instructions are available [here](https://rdflib.readthedocs.io/en/stable/gettingstarted.html).

- [VS Studio Code](https://code.visualstudio.com/) (optional, a code editor with extensions for RDF formats like TTL and JSON-LD)
  - Installation instructions are available [here](https://code.visualstudio.com/download).

### Quick Start

To quickly explore and make use of the ontology, first download the pre-inferred version [pre-inferred ontology](inferred_version/battery-inferred.ttl). You can then simply open the file in Protégé and explore its content or load the ontology into python using EMMOntoPy.

In [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy), you can choose to import the ontology from your local downloaded copy or directly from the web. Commands for both options are given below:

```python
from ontopy import get_ontology

# Loading from local repository
battery = get_ontology('/path/to/domain-battery/battery-inferred.ttl').load(url_from_catalog=True)

# Loading from web
battery = get_ontology('https://raw.githubusercontent.com/emmo-repo/domain-battery/master/inferred_version/battery-inferred.ttl').load()
```

## Contributing

We welcome contributions from the community to enhance and expand the ontology. If you have suggestions, improvements, or additional chemical substance information to contribute, please refer to our [Contribution Guidelines](CONTRIBUTING.md).

### Acknowledgements

<img src="docs/assets/images/flag_of_europe.png" alt="EU-Flag" width="100">

This project has received support from European Union research and innovation programs, under grant agreement numbers:

* 957189 - [BIG-MAP](http://www.big-map.eu/) 

## License

The Battery Interface Domain Ontology is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license (CC BY 4.0)

[1]: https://github.com/emmo-repo/EMMO
[2]: https://www.big-map.eu

