[![FOOPS Score](https://img.shields.io/badge/FOOPS%20Score-75.0%25-brightgreen)](https://foops.linkeddata.es/FAIR_validator.html)
![reason](https://github.com/emmo-repo/domain-battery/actions/workflows/reason.yml/badge.svg)
![docs](https://github.com/emmo-repo/domain-battery/actions/workflows/doc.yml/badge.svg)
[![unstable](http://badges.github.io/stability-badges/dist/unstable.svg)](http://github.com/badges/stability-badges)  

[![DOI](https://zenodo.org/badge/570454101.svg)](https://zenodo.org/badge/latestdoi/570454101)

<!-- markdownlint-disable MD033 -->

# Battery Domain Ontology

<img src="docs/assets/img/fig/svg/domain-battery-logo.svg" alt="domain-battery-logo" width="100%">

<!-- [![CI tests](https://github.com/emmo-repo/domain-battery/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-battery/actions/) -->
The Battery Domain Ontology is a domain of the [Elementary Multiperspective Materials Ontology (EMMO)][1], for describing battery systems, materials, methods, and data. Its primary objective is to support the creation of [FAIR](https://www.go-fair.org/fair-principles/), [Linked Data](https://en.wikipedia.org/wiki/Linked_data). This ontology serves as a foundational resource for harmonizing battery knowledge representation, enhancing data interoperability, and accelerating progress in battery research and innovation.

Reference documentation is available [here](https://emmo-repo.github.io/domain-battery/index.html)
 
# Quick Start

Here is some information to help you get started working with the ontology in python and creating you own instances of Linked Data. For more information, please see the [Getting Started](https://emmo-repo.github.io/domain-battery/pages/getstarted.html) and [Examples](https://emmo-repo.github.io/domain-battery/pages/examples.html) section of the documentation. 

## Reference IRIs

The table below contains a quick cheat sheet of IRIs for accessing different files from the ontology
The import structure is summarized in the following table:

| IRI                                                   | Description                   |
| ----------------------------------------------------- | ----------------------------- |
| `https://w3id.org/emmo/domain/battery`                | Base Asserted Ontology*       |
| `https://w3id.org/emmo/domain/battery/inferred`       | Base Pre-Inferred Ontology*   |
| `https://w3id.org/emmo/domain/battery/latest`         | Latest Asserted Ontology*     |
| `https://w3id.org/emmo/domain/battery/source`         | Source of Asserted Ontology*  |
| `https://w3id.org/emmo/domain/battery/context`        | Latest JSON-LD Context File   |
| `https://w3id.org/emmo/domain/battery/{VERSION}`      | Version of Asserted Ontology* |
| `https://w3id.org/emmo/domain/battery/{VERSION}/...`  | ... follows same logic above  |

*IRI directs to human readable documentation if called from the web browser and to the source .ttl file if called from an application

## Python
There are two common ways to work with the ontology in python: loading the ontology as a graph using [rdflib](https://rdflib.readthedocs.io/en/stable/) or exploring the content of the ontology using [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy). Examples of both are provided below.

### rdflib
In [rdflib](https://rdflib.readthedocs.io/en/stable/), you can import the ontology as a graph, e.g. to run SPARQL queries:

```python
from rdflib import Graph

# Define the IRI of the ontology
echo = "https://w3id.org/emmo/domain/battery"

# Create an empty graph
g = Graph()

# Load the ontology from the IRI
g.parse(echo, format="ttl")

# Print the number of triples in the graph
print(f"Graph has {len(g)} triples.")
```
### EMMOntoPy
In [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy), you can choose to import the ontology directly from the web:

```python
from ontopy import get_ontology

# Loading from web
echo = get_ontology('https://w3id.org/emmo/domain/battery').load()
```

## Usage

This domain ontology supports the creation of Linked Data in any RDF-supported format. Below is an example using [JSON-LD](https://json-ld.org/) to desecribe a zinc foil electrode with some creator information and properties. Please see the documentation for [more examples](https://emmo-repo.github.io/domain-battery/pages/examples.html). 

```json
{
    "@context": "https://w3id.org/emmo/domain/battery/context",
    "@type": "CR2032",
    "schema:name": "My CR2032 Coin Cell",
    "schema:manufacturer": {
       "@id": "https://www.wikidata.org/wiki/Q3041255",
       "schema:name": "SINTEF"
    },
    "hasProperty": {
       "@type": ["NominalCapacity", "ConventionalProperty"],
       "hasNumericalPart": {
          "@type": "Real",
          "hasNumericalValue": 230
        },
        "hasMeasurementUnit": "emmo:MilliAmpereHour"
     }
}
```

### Acknowledgements

<img src="docs/assets/img/Flag_of_Europe.png" alt="EU-Flag" width="100">

This project has received support from European Union research and innovation programs, under grant agreement numbers:

* [957189 - BIG-MAP](http://www.big-map.eu/)
* [101104022 - Battery2030+](https://battery2030.eu/) 
* [101103997 - DigiBatt](https://digibattproject.eu/)

## License

The Battery Domain Ontology is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license (CC BY 4.0).

[1]: https://github.com/emmo-repo/EMMO
[2]: https://www.big-map.eu
