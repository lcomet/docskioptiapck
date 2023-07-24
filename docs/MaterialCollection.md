# Class: MaterialCollection


_A holder for Material objects_





URI: [kioptipack_schema:MaterialCollection](https://w3id.org/Fraunhofer/kioptipack-schema/MaterialCollection)



```mermaid
 classDiagram
    class MaterialCollection
      MaterialCollection : entries
        
          MaterialCollection --|> Material : entries
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entries](entries.md) | 0..* <br/> [Material](Material.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/Fraunhofer/kioptipack-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kioptipack_schema:MaterialCollection |
| native | kioptipack_schema:MaterialCollection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialCollection
description: A holder for Material objects
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
    rank: 1000
    multivalued: true
    range: Material
    inlined: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: MaterialCollection
description: A holder for Material objects
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
    rank: 1000
    multivalued: true
    alias: entries
    owner: MaterialCollection
    domain_of:
    - MaterialCollection
    range: Material
    inlined: true
tree_root: true

```
</details>