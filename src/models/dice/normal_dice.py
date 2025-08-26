from typing import override

from commom.providers.random_provider import RandomProvider
from .base_dice import BaseDice


class NormalDice(BaseDice):
    def __init__(self, faces: int):
        self._random_provider = RandomProvider()
        self._faces = faces


    @override
    def roll(self) -> int:
        random = self._random_provider.getRandom()

        return random.randint(1, self._faces)
