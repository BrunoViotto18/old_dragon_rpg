
from abc import ABC, abstractmethod


class Attributes(ABC):

    @property
    @abstractmethod
    def power(self) -> int:
        pass

    @property
    @abstractmethod
    def dexterity(self) -> int:
        pass

    @property
    @abstractmethod
    def constitution(self) -> int:
        pass

    @property
    @abstractmethod
    def intelligence(self) -> int:
        pass

    @property
    @abstractmethod
    def wisdom(self) -> int:
        pass

    @property
    @abstractmethod
    def charisma(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
