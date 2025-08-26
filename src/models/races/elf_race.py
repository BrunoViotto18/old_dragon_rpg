
from typing import override
from models.races.race import Race


class ElfRace(Race):

    @property
    @override
    def name(self) -> str:
        return 'Elfo'


    @property
    @override
    def movement(self) -> int:
        return 9


    @property
    @override
    def infravision(self) -> int:
        return 18


    @property
    @override
    def alignment(self) -> str:
        return 'Neutro'
