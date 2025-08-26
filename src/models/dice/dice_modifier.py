from typing import override
from .base_dice import BaseDice
from .dice import Dice


class DiceModifier(BaseDice):
    def __init__(self, dice: Dice, modifier: int):
        self._dice = dice
        self._modifier = modifier


    @override
    def roll(self) -> int:
        return self._dice.roll() + self._modifier
