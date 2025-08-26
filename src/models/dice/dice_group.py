from typing import override

from models.dice.dice_collection import DiceCollection
from .dice import Dice


class DiceGroup(DiceCollection):
    def __init__(self, dice: list[Dice]):
        self._dice = dice


    @override
    def roll(self) -> int:
        return self.roll_ignore_smallest(0)


    @override
    def roll_ignore_smallest(self, amount_to_ignore: int = 1) -> int:
        values = [dice.roll() for dice in self._dice]
        return sum(DiceGroup._ignore_smallest(values, amount_to_ignore))


    @staticmethod
    def _ignore_smallest(values: list[int], amount_to_ignore: int) -> list[int]:
        values.sort()

        return values[amount_to_ignore:]
