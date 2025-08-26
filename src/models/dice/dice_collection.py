
from abc import abstractmethod
from models.dice.base_dice import BaseDice


class DiceCollection(BaseDice):

    @abstractmethod
    def roll(self) -> int:
        pass


    @abstractmethod
    def roll_ignore_smallest(self, amount_to_ignore: int = 1) -> int:
        pass
