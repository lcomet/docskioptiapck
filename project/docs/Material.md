
# Class: Material


The material may contain one or more distinguish additives, recyclates or virgin materials.

URI: [kioptipack_schema:Material](https://w3id.org/Fraunhofer/kioptipack-schema/Material)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VirginMaterial],[Recyclate],[NamedThing],[Material&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[VirginMaterial],[Material]^-[Recyclate],[Material]^-[Additive],[NamedThing]^-[Material],[Additive])](https://yuml.me/diagram/nofunky;dir:TB/class/[VirginMaterial],[Recyclate],[NamedThing],[Material&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[VirginMaterial],[Material]^-[Recyclate],[Material]^-[Additive],[NamedThing]^-[Material],[Additive])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Children

 * [Additive](Additive.md) - This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es).
 * [Recyclate](Recyclate.md) - This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es).
 * [VirginMaterial](VirginMaterial.md) - Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this material with one chemical structure/molecule.

## Referenced by Class


## Attributes


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
