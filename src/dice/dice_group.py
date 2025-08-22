from typing import override
from .base_dice import BaseDice
from .dice import Dice


class DiceGroup(BaseDice):
    def __init__(self, dice: list[Dice]):
        self._dice = dice


    @override
    def roll(self) -> int:
        sum = 0
        for dice in self._dice:
            sum += dice.roll()

        return sum
