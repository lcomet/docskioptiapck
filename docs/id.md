# Slot: id


_A unique identifier for a thing_



URI: [schema:identifier](http://schema.org/identifier)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
[Material](Material.md) | The material may contain one or more distinguish additives, recyclates or vir... |  no  |
[Additive](Additive.md) | This class contain different sub classes to make additives more specific |  no  |
[Recyclate](Recyclate.md) | This class contain different sub classes to make additives more specific |  no  |
[VirginMaterial](VirginMaterial.md) | Virgin materials are all materials, which contain only one kind of material |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/Fraunhofer/kioptipack-schema




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
rank: 1000
slot_uri: schema:identifier
identifier: true
alias: id
domain_of:
- NamedThing
range: uriorcurie
required: true

```
</details>