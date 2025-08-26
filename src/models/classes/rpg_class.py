from abc import ABC, abstractmethod


class RpgClass(ABC):

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
