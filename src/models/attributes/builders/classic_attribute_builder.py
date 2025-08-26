from typing import override
from models.attributes.attributes import Attributes
from models.attributes.builders.base_attribute_builder import BaseAttributeBuilder
from models.attributes.character_attributes import CharacterAttributes
from models.dice.dice_factory import DiceFactory


class ClassicAttributeBuilder(BaseAttributeBuilder):

    def __init__(self):
        self._dice_factory = DiceFactory()
        self._values: list[int] = []


    @override
    def generate_values(self) -> list[int]:
        _3d6 = self._dice_factory.create_d6() * 3
        self._values = [_3d6.roll() for _ in range(6)]
        return self._values[:]


    @override
    def build(self) -> Attributes:
        if (len(self._values) != 6):
            raise NotImplementedError()

        if     self._power is None\
            or self._dexterity is None\
            or self._constitution is None\
            or self._intelligence is None\
            or self._wisdom is None\
            or self._charisma is None:

            raise NotImplementedError()

        values = [self._power, self._dexterity, self._constitution, self._intelligence, self._wisdom, self._charisma]

        for i in range(6):
            if values[i] != self._values[i]:
                raise NotImplementedError()

        return CharacterAttributes(self._power, self._dexterity, self._constitution, self._intelligence, self._wisdom, self._charisma)
