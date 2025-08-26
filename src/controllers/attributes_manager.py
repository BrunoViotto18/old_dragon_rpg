
from models.dice.dice_factory import DiceFactory


class AttributesManager:
    def __init__(self):
        self._dice_factory = DiceFactory()


    def generate_classic_values(self) -> list[int]:
        _3d6 = self._dice_factory.create_d6() * 3
        return [_3d6.roll() for _ in range(6)]


    def generate_adventurer_values(self) -> list[int]:
        _3d6 = self._dice_factory.create_d6() * 3
        return [_3d6.roll() for _ in range(6)]


    def generate_heroic_values(self) -> list[int]:
        _4d6 = self._dice_factory.create_d6() * 4
        return [_4d6.roll_ignore_smallest() for _ in range(6)]


    @staticmethod
    def _ignore_smaller(numbers: list[int]) -> list[int]:
        if (len(numbers) == 0):
            return []

        smaller = min(numbers)

        numbers.remove(smaller)

        return numbers
