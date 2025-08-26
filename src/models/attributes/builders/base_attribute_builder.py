
from abc import abstractmethod
from typing import override
from models.attributes.attributes import Attributes
from models.attributes.builders.attribute_builder import AttributeBuilder


class BaseAttributeBuilder(AttributeBuilder):

    def __init__(self):
        self._power: int | None = None
        self._dexterity: int | None = None
        self._constitution: int | None = None
        self._intelligence: int | None = None
        self._wisdom: int | None = None
        self._charisma: int | None = None


    @abstractmethod
    def generate_values(self) -> list[int]:
        pass


    @abstractmethod
    def build(self) -> Attributes:
        pass


    @override
    def with_power(self, power: int) -> AttributeBuilder:
        self._power = power
        return self


    @override
    def with_dexterity(self, dexterity: int) -> AttributeBuilder:
        self._dexterity = dexterity
        return self


    @override
    def with_constitution(self, constitution: int) -> AttributeBuilder:
        self._constitution = constitution
        return self


    @override
    def with_intelligence(self, intelligence: int) -> AttributeBuilder:
        self._intelligence = intelligence
        return self


    @override
    def with_wisdom(self, wisdom: int) -> AttributeBuilder:
        self._wisdom = wisdom
        return self


    @override
    def with_charisma(self, charisma: int) -> AttributeBuilder:
        self._charisma = charisma
        return self
