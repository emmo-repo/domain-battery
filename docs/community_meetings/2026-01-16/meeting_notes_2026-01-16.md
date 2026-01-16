# BattINFO community meeting notes - 2026-01-16

- Update on simplified notation for expressing quantities
- How to support validation of instances and updates of breaking changes
    - Parse battery metadata --> instantiate and run simulation
- Discussion on how detailed semantic descriptions of parthood need to be (e.g. just saying that something is a part of something else v. giving really detailed description of the role that it plays and interactions)

## Quantity Notation

EMMO is discussing simplifications to the way that quantities are expressed, in order to avoid the case that a knowledge graph has to contain individuals for every number. To get around this, we treat the quantity as both a quantity and a numerical:

#### NEW

For Scalars

"hasProperty": {
    "@type": "Voltage",
    "hasNumberValue": 3.9,
    "hasMeasurementUnit": "emmo:Volt"
}

For Arrays / Vectors

"hasProperty": {
    "@type": ["Acceleration", "Vector"],
    "hasNumberValue": [9.81, 0, 0],
    "hasMeasurementUnit": "emmo:MetrePerSquareSecond"
}

#### OLD:

"hasProperty": {
    "@type": "Voltage",
    "hasNumericalPart": {
        "@type": "RealData",
        "hasNumberValue": 3.9,
    }
    "hasMeasurementUnit": "emmo:Volt"
}

## Electrode-Electrolyte Interfaces

{
    "@type:" Cathode,
    "contacts":{
        "@type": "Catholyte"
    }
}

## Next Steps

- Validation of instances, how to make this more robust? The native way to do it is with SHACL, but also that could be done with 

- Do an example of SoldiStateBattery and look into if there are any semantic differences that are necessary to describe how the electrode interacts with the electrolyte?

- Prepare some examples of how to parse and use the battery and dataset metadata for simulations and / or automated analysis. 