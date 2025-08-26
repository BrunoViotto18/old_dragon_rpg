
from typing import override
from models.classes.rpg_class import RpgClass


class WarriorClass(RpgClass):

    @property
    @override
    def name(self) -> str:
        return 'Guerreiro'


    @property
    @override
    def health(self) -> int:
        return 10


    @property
    @override
    def attack(self) -> int:
        return 1


    @property
    @override
    def weapons(self) -> list[str]:
        return ['Todas']


    @property
    @override
    def armors(self) -> list[str]:
        return ['Todas']


    @property
    @override
    def magic_items(self) -> list[str]:
        return ['Pergaminhos de proteção']


    @override
    def get_skills(self):
        return ['Aparar', 'Maestria em Armas']
