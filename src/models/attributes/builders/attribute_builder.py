from __future__ import annotations
from abc import abstractmethod

from models.attributes.attributes import Attributes


class AttributeBuilder:

    @abstractmethod
    def generate_values(self) -> list[int]:
        pass


    @abstractmethod
    def build(self) -> Attributes:
        pass


    @abstractmethod
    def with_power(self, power: int) -> AttributeBuilder:
        pass


    @abstractmethod
    def with_dexterity(self, dexterity: int) -> AttributeBuilder:
        pass


    @abstractmethod
    def with_constitution(self, constitution: int) -> AttributeBuilder:
        pass


    @abstractmethod
    def with_intelligence(self, intelligence: int) -> AttributeBuilder:
        pass


    @abstractmethod
    def with_wisdom(self, wisdom: int) -> AttributeBuilder:
        pass


    @abstractmethod
    def with_charisma(self, charisma: int) -> AttributeBuilder:
        pass
