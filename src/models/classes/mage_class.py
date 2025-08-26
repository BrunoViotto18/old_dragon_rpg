from typing import override

from models.classes.rpg_class import RpgClass


class MageClass(RpgClass):

    @property
    @override
    def name(self) -> str:
        return 'Mago'


    @property
    @override
    def health(self) -> int:
        return 4


    @property
    @override
    def attack(self) -> int:
        return 0


    @property
    @override
    def weapons(self) -> list[str]:
        return ['Armas pequenas', 'Armas cortantes', 'Armas perfurantes']


    @property
    @override
    def armors(self) -> list[str]:
        return ['Nenhuma']


    @property
    @override
    def magic_items(self) -> list[str]:
        return ['Todos']


    @override
    def get_skills(self):
        return ['Magias Arcanas', 'Ler Magias', 'Detectar Magias']
