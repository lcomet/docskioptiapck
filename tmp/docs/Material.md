
# Class: Material


The material may contain one or more distinguish additives, recyclates or virgin materials.

URI: [kioptipack_schema:Material](https://w3id.org/Fraunhofer/kioptipack-schema/Material)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[MaterialCollection]++-%20entries%200..*>[Material&#124;primary_email:string%20%3F;birth_date:date%20%3F;age_in_years:integer%20%3F;vital_status:PersonStatus%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[Material],[MaterialCollection])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[MaterialCollection]++-%20entries%200..*>[Material&#124;primary_email:string%20%3F;birth_date:date%20%3F;age_in_years:integer%20%3F;vital_status:PersonStatus%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[Material],[MaterialCollection])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **None** *[➞entries](materialCollection__entries.md)*  <sub>0..\*</sub>  **[Material](Material.md)**

## Attributes


### Own

 * [Material➞primary_email](Material_primary_email.md)  <sub>0..1</sub>
     * Description: The main email address of a person
     * Range: [String](types/String.md)
 * [birth_date](birth_date.md)  <sub>0..1</sub>
     * Description: Date on which a person is born
     * Range: [Date](types/Date.md)
 * [age_in_years](age_in_years.md)  <sub>0..1</sub>
     * Description: Number of years since birth
     * Range: [Integer](types/Integer.md)
 * [vital_status](vital_status.md)  <sub>0..1</sub>
     * Description: living or dead status
     * Range: [PersonStatus](PersonStatus.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)
