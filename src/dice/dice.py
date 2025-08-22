from __future__ import annotations
from abc import ABC, abstractmethod

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
    def __mul__(self, amount: int) -> Dice:
        pass

    @abstractmethod
    def __rmul__(self, amount: int) -> Dice:
        pass

    @abstractmethod
    def __imul__(self, amount: int) -> Dice:
        pass
