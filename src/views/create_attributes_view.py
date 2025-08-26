from typing import override

from models.attributes.attributes import Attributes
from .attributes.adventurer_attribute_view import AdventurerAttributeView
from .attributes.classic_attribute_view import ClassicAttributeView
from views.attributes.heroic_attribute_view import HeroicAttributeView
from views.menus.menu_option import MenuOption
from views.menus.menu_view import MenuView


class CreateAttributesView(MenuView[Attributes]):

    def __init__(self):
        super().__init__()


    @override
    def get_options(self) -> list[MenuOption[Attributes]]:
        return [
            MenuOption('Clássico', ClassicAttributeView()),
            MenuOption('Aventureiro', AdventurerAttributeView()),
            MenuOption('Aventureiro', HeroicAttributeView())
        ]
