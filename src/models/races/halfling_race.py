from typing import override
from models.races.race import Race


class HalflingRace(Race):

    @property
    @override
    def movement(self) -> int:
        return 6


    @property
    @override
    def infravision(self) -> int:
        return 0


    @property
    @override
    def alignment(self) -> None:
        raise NotImplementedError()
