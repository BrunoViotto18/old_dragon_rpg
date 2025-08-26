from models.attributes.attributes import Attributes
from models.classes.rpg_class import RpgClass
from models.races.race import Race


class Character:

    def __init__(self, name: str, attributes: Attributes, race: Race, rpg_class: RpgClass):
        self._name = name
        self._hp = rpg_class.health

        self._attributes = attributes
        self._race = race
        self._rpg_class = rpg_class


    @property
    def name(self) -> str:
        return self._name


    @property
    def hp(self) -> int:
        return self._hp


    @property
    def attributes(self) -> Attributes:
        return self._attributes


    @property
    def race(self) -> Race:
        return self._race


    @property
    def rpg_class(self) -> RpgClass:
        return self._rpg_class
