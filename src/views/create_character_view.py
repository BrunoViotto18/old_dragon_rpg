
from typing import override
from models.characters.character import Character
from views.create_attributes_view import CreateAttributesView
from views.base_view import BaseView
from views.create_class_view import CreateClassView
from views.create_race_view import CreateRaceView
from views.display_character_view import DisplayCharacterView


class CreateCharacterView(BaseView[Character]):

    @override
    def on_show(self):
        name = input('Digite o nome do personagem: ')

        create_attributes_view = CreateAttributesView()
        create_class_view = CreateClassView()
        create_race_view = CreateRaceView()

        create_attributes_view.show()
        attributes = create_attributes_view.get_output()

        if attributes is None:
            raise NotImplementedError()

        create_race_view.show()
        race = create_race_view.get_output()

        if race is None:
            raise NotImplementedError()

        create_class_view.show()
        rpg_class = create_class_view.get_output()

        if rpg_class is None:
            raise NotImplementedError()

        character = Character(name, attributes, race, rpg_class)
        self._output = character

        display_character_view = DisplayCharacterView(character)
        display_character_view.show()
