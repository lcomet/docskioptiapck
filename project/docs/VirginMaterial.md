
# Class: Virgin Material


Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this material with one chemical structure/molecule.

URI: [kioptipack_schema:VirginMaterial](https://w3id.org/Fraunhofer/kioptipack-schema/VirginMaterial)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Material]^-[VirginMaterial&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Material])](https://yuml.me/diagram/nofunky;dir:TB/class/[Material]^-[VirginMaterial&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Material])

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
