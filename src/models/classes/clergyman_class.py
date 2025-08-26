from typing import override

from models.classes.rpg_class import RpgClass


class ClergymanClass(RpgClass):

    @property
    @override
    def name(self) -> str:
        return 'Clérigo'


    @property
    @override
    def weapons(self) -> list[str]:
        return ['Armas impactantes', 'Armas cortantes', 'Armas perfurantes']


    @property
    @override
    def armors(self) -> list[str]:
        return ['Todas']


    @property
    @override
    def magic_items(self) -> list[str]:
        return ['Todos']


    @override
    def get_skills(self):
        return ['Magias Divinas', 'Afastar Mortos-Vivos', 'Cura Milagrosa']
