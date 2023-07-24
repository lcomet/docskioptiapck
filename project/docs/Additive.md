
# Class: Additive


This class contain different sub classes to make additives more specific. In general, there are no instances of this class, but from the subclass(es).

URI: [kioptipack_schema:Additive](https://w3id.org/Fraunhofer/kioptipack-schema/Additive)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Material],[Material]^-[Additive&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Material],[Material]^-[Additive&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [Material](Material.md) - The material may contain one or more distinguish additives, recyclates or virgin materials.

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)

### Inherited from Material:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
