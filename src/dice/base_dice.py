from abc import abstractmethod
from typing import override
from .dice import Dice


class BaseDice(Dice):
    @abstractmethod
    def roll(self) -> int:
        pass


    @override
    def __add__(self, modifier: int) -> Dice:
        from .dice_modifier import DiceModifier
        return DiceModifier(self, modifier)


    @override
    def __radd__(self, modifier: int) -> Dice:
        return self + modifier


    @override
    def __iadd__(self, modifier: int) -> Dice:
        return self + modifier


    @override
    def __mul__(self, amount: int) -> Dice:
        from .dice_group import DiceGroup
        return DiceGroup([self for _ in range(amount)])


    @override
    def __rmul__(self, amount: int) -> Dice:
        return self * amount


    @override
    def __imul__(self, amount: int) -> Dice:
        return self * amount
