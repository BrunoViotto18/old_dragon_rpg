from abc import ABC, abstractmethod


class RpgClass(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def health(self) -> int:
        pass

    @property
    @abstractmethod
    def attack(self) -> int:
        pass

    @property
    @abstractmethod
    def weapons(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def armors(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def magic_items(self) -> list[str]:
        pass

    @abstractmethod
    def get_skills(self) -> list[str]:
        pass
