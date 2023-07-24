# Enum: PersonStatus



URI: [PersonStatus](PersonStatus)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ALIVE | None | the person is living |
| DEAD | None | the person is deceased |
| UNKNOWN | None | the vital status is not known |




## Slots

| Name | Description |
| ---  | --- |
| [vital_status](vital_status.md) | living or dead status |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/Fraunhofer/kioptipack-schema




## LinkML Source

<details>
```yaml
name: PersonStatus
from_schema: https://w3id.org/Fraunhofer/kioptipack-schema
rank: 1000
permissible_values:
  ALIVE:
    text: ALIVE
    description: the person is living
  DEAD:
    text: DEAD
    description: the person is deceased
  UNKNOWN:
    text: UNKNOWN
    description: the vital status is not known
    todos:
    - map this to an ontology

```
</details>
