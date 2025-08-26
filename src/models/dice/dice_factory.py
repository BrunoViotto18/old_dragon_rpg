from .dice import Dice
from .normal_dice import NormalDice


class DiceFactory:
    def create_d4(self) -> Dice:
        return NormalDice(4)


    def create_d6(self) -> Dice:
        return NormalDice(6)


    def create_d8(self) -> Dice:
        return NormalDice(8)


    def create_d10(self) -> Dice:
        return NormalDice(10)


    def create_d12(self) -> Dice:
        return NormalDice(12)


    def create_d20(self) -> Dice:
        return NormalDice(20)


    def create_custom(self, amount: int, faces: int, modifier: int):
        return amount * NormalDice(faces) + modifier
