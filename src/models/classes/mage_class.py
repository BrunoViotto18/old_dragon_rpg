
from abc import abstractmethod

from models.classes.rpg_class import RpgClass


class MageClass(RpgClass):

    @property
    @abstractmethod
    def weapons(self) -> list[str]:
        return ['Armas pequenas', 'Armas cortantes', 'Armas perfurantes']

    @property
    @abstractmethod
    def armors(self) -> list[str]:
        return ['Nenhuma']

    @property
    @abstractmethod
    def magic_items(self) -> list[str]:
        return ['Todos']

    @abstractmethod
    def get_skills(self):
        return ['Magias Arcanas', 'Ler Magias', 'Detectar Magias']
