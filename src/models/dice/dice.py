from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.dice.dice_collection import DiceCollection
    

class Dice(ABC):
    @abstractmethod
    def roll(self) -> int:
        pass

    @abstractmethod
    def __add__(self, modifier: int) -> Dice:
        pass

    @abstractmethod
    def __radd__(self, modifier: int) -> Dice:
        pass

    @abstractmethod
    def __iadd__(self, modifier: int) -> Dice:
        pass

    @abstractmethod
    def __mul__(self, amount: int) -> DiceCollection:
        pass

    @abstractmethod
    def __rmul__(self, amount: int) -> DiceCollection:
        pass

    @abstractmethod
    def __imul__(self, amount: int) -> DiceCollection:
        pass
