
from abc import ABC, abstractmethod


class Race(ABC):

    @property
    @abstractmethod
    def movement(self) -> int:
        pass

    @property
    @abstractmethod
    def infravision(self) -> int:
        pass

    @property
    @abstractmethod
    def alignment(self) -> None:
        pass
