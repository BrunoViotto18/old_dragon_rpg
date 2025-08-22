from random import Random


class RandomProvider:
    _instance: Random | None = None


    def getRandom(self) -> Random:
        if RandomProvider._instance is None:
            RandomProvider._instance = Random()

        return RandomProvider._instance
