
from abc import abstractmethod
from models.classes.rpg_class import RpgClass


class WarriorClass(RpgClass):

    @property
    @abstractmethod
    def weapons(self) -> list[str]:
        return ['Todas']

    @property
    @abstractmethod
    def armors(self) -> list[str]:
        return ['Todas']

    @property
    @abstractmethod
    def magic_items(self) -> list[str]:
        return ['Pergaminhos de proteção']

    @abstractmethod
    def get_skills(self):
        return ['Aparar', 'Maestria em Armas']
