# kioptipack-schema

Documentation of the ontology and metamodels for the KIOptipack project

URI: https://w3id.org/Fraunhofer/kioptipack-schema

Name: kioptipack-schema



## Classes

| Class | Description |
| --- | --- |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Material](Material.md) | The material may contain one or more distinguish additives, recyclates or virgin materials. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Additive](Additive.md) | This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Recyclate](Recyclate.md) | This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VirginMaterial](VirginMaterial.md) | Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this material with one chemical structure/molecule. |



## Slots

| Slot | Description |
| --- | --- |
| [age_in_years](age_in_years.md) | Number of years since birth |
| [birth_date](birth_date.md) | Date on which a person is born |
| [description](description.md) | A human-readable description for a thing |
| [id](id.md) | A unique identifier for a thing |
| [name](name.md) | A human-readable name for a thing |
| [primary_email](primary_email.md) | The main email address of a person |
| [vital_status](vital_status.md) | living or dead status |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [PersonStatus](PersonStatus.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
