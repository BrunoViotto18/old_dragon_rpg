from typing import override
from models.races.race import Race


class DwarfRace(Race):

    @property
    @override
    def movement(self) -> int:
        return 6


    @property
    @override
    def infravision(self) -> int:
        return 18


    @property
    @override
    def alignment(self) -> None:
        raise NotImplementedError()
