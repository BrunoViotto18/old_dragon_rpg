
from abc import abstractmethod

from models.classes.rpg_class import RpgClass


class ClergymanClass(RpgClass):

    @property
    @abstractmethod
    def weapons(self) -> list[str]:
        return ['Armas impactantes', 'Armas cortantes', 'Armas perfurantes']

    @property
    @abstractmethod
    def armors(self) -> list[str]:
        return ['Todas']

    @property
    @abstractmethod
    def magic_items(self) -> list[str]:
        return ['Todos']

    @abstractmethod
    def get_skills(self):
        return ['Magias Divinas', 'Afastar Mortos-Vivos', 'Cura Milagrosa']
