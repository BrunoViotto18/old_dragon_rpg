
from typing import override

from .attributes import Attributes


class CharacterAttributes(Attributes):

    def __init__(self, power: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int):
        self._power = power
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma


    @property
    @override
    def power(self) -> int:
        return self._power


    @property
    @override
    def dexterity(self) -> int:
        return self._dexterity


    @property
    @override
    def constitution(self) -> int:
        return self._constitution


    @property
    @override
    def intelligence(self) -> int:
        return self._intelligence


    @property
    @override
    def wisdom(self) -> int:
        return self._wisdom


    @property
    @override
    def charisma(self) -> int:
        return self._charisma


    @override
    def __str__(self) -> str:
        return f'{{ power: {self._power}, dexterity: {self._dexterity}, constitution: {self._constitution}, intelligence: {self._intelligence}, wisdom: {self._wisdom}, charisma: {self._charisma} }}'
