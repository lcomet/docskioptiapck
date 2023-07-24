# Auto generated from kioptipack_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-24T12:34:34
# Schema: kioptipack-schema
#
# id: https://w3id.org/Fraunhofer/kioptipack-schema
# description: Documentation of the ontology and metamodels for the KIOptipack project
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
KIOPTIPACK_SCHEMA = CurieNamespace('kioptipack_schema', 'https://w3id.org/Fraunhofer/kioptipack-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = KIOPTIPACK_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class MaterialId(NamedThingId):
    pass


class AdditiveId(MaterialId):
    pass


class RecyclateId(MaterialId):
    pass


class VirginMaterialId(MaterialId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Material(NamedThing):
    """
    The material may contain one or more distinguish additives, recyclates or virgin materials.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Material
    class_class_curie: ClassVar[str] = "kioptipack_schema:Material"
    class_name: ClassVar[str] = "Material"
    class_model_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Material

    id: Union[str, MaterialId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialId):
            self.id = MaterialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Additive(Material):
    """
    This class contain different sub classes to make additives more specific. In general, there are no instances of
    this class, but from the subclass(es).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Additive
    class_class_curie: ClassVar[str] = "kioptipack_schema:Additive"
    class_name: ClassVar[str] = "Additive"
    class_model_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Additive

    id: Union[str, AdditiveId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdditiveId):
            self.id = AdditiveId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Recyclate(Material):
    """
    This class contain different sub classes to make additives more specific. In general, there are no instances of
    this class, but from the subclass(es).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Recyclate
    class_class_curie: ClassVar[str] = "kioptipack_schema:Recyclate"
    class_name: ClassVar[str] = "Recyclate"
    class_model_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.Recyclate

    id: Union[str, RecyclateId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecyclateId):
            self.id = RecyclateId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class VirginMaterial(Material):
    """
    Virgin materials are all materials, which contain only one kind of material. You should be able, to describe this
    material with one chemical structure/molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.VirginMaterial
    class_class_curie: ClassVar[str] = "kioptipack_schema:VirginMaterial"
    class_name: ClassVar[str] = "Virgin Material"
    class_model_uri: ClassVar[URIRef] = KIOPTIPACK_SCHEMA.VirginMaterial

    id: Union[str, VirginMaterialId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirginMaterialId):
            self.id = VirginMaterialId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living")
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=KIOPTIPACK_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=KIOPTIPACK_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=KIOPTIPACK_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=KIOPTIPACK_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=KIOPTIPACK_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=KIOPTIPACK_SCHEMA.age_in_years, name="age_in_years", curie=KIOPTIPACK_SCHEMA.curie('age_in_years'),
                   model_uri=KIOPTIPACK_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=KIOPTIPACK_SCHEMA.vital_status, name="vital_status", curie=KIOPTIPACK_SCHEMA.curie('vital_status'),
                   model_uri=KIOPTIPACK_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])