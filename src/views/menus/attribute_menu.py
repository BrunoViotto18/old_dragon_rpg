from typing import override
from views.adventurer_attribute_view import AdventurerAttributeView
from views.classic_attribute_view import ClassicAttributeView
from views.heroic_attribute_view import HeroicAttributeView
from views.menus.menu_option import MenuOption
from views.menus.menu_view import MenuView


class AttributeMenu(MenuView):

    @override
    def get_options(self) -> list[MenuOption]:
        return [
            MenuOption('Clássico', ClassicAttributeView()),
            MenuOption('Aventureiro', AdventurerAttributeView()),
            MenuOption('Aventureiro', HeroicAttributeView())
        ]
