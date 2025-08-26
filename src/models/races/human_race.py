
from typing import override
from models.races.race import Race


class HumanRace(Race):

    @property
    @override
    def name(self) -> str:
        return 'Humano'


    @property
    @override
    def movement(self) -> int:
        return 9


    @property
    @override
    def infravision(self) -> int:
        return 0


    @property
    @override
    def alignment(self) -> str:
        return 'Qualquer'
