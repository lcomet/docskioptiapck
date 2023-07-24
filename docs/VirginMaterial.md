# Class: VirginMaterial


_Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this material with one chemical structure/molecule._





URI: [kioptipack_schema:VirginMaterial](https://w3id.org/Fraunhofer/kioptipack-schema/VirginMaterial)



```mermaid
 classDiagram
    class VirginMaterial
      Material <|-- VirginMaterial
      
      VirginMaterial : description
        
      VirginMaterial : id
        
      VirginMaterial : name
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Material](Material.md)
        * **VirginMaterial**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/Fraunhofer/kioptipack-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kioptipack_schema:VirginMaterial |
| native | kioptipack_schema:VirginMaterial |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Virgin Material
description: Virgin materials are all materials, which contain only one kind of material.
  You should be able, to describe this material with one chemical structure/molecule.
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
is_a: Material
slots:
- name
- description

```
</details>

### Induced

<details>
```yaml
name: Virgin Material
description: Virgin materials are all materials, which contain only one kind of material.
  You should be able, to describe this material with one chemical structure/molecule.
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
is_a: Material
attributes:
  name:
    name: name
    description: A human-readable name for a thing
    from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Virgin Material
    domain_of:
    - NamedThing
    - Additive
    - Recyclate
    - Virgin Material
    range: string
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: Virgin Material
    domain_of:
    - NamedThing
    - Additive
    - Recyclate
    - Virgin Material
    range: string
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Virgin Material
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true

```
</details>