
# kioptipack-schema


**metamodel version:** 1.7.0

**version:** None


Documentation of the ontology and metamodels for the KIOptipack project


### Classes

 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [Material](Material.md) - The material may contain one or more distinguish additives, recyclates or virgin materials.
         * [Additive](Additive.md) - This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es).
         * [Recyclate](Recyclate.md) - This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es).
         * [VirginMaterial](VirginMaterial.md) - Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this material with one chemical structure/molecule.

### Mixins


### Slots

 * [age_in_years](age_in_years.md) - Number of years since birth
 * [birth_date](birth_date.md) - Date on which a person is born
 * [description](description.md) - A human-readable description for a thing
 * [id](id.md) - A unique identifier for a thing
 * [name](name.md) - A human-readable name for a thing
 * [primary_email](primary_email.md) - The main email address of a person
 * [vital_status](vital_status.md) - living or dead status

### Enums

 * [PersonStatus](PersonStatus.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
