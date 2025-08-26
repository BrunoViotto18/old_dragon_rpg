
from abc import ABC, abstractmethod


class Race(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass


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
    def alignment(self) -> str:
        pass

    @property
    @abstractmethod
    def skills(self) -> list[str]:
        pass
