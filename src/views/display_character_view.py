from typing import override
from models.characters.character import Character
from views.base_view import BaseView


class DisplayCharacterView(BaseView[None]):

    def __init__(self, character: Character):
        super().__init__()
        self._character = character


    @override
    def on_show(self):
        print(f'Nome: {self._character.name}')

        print()
        print(f'# Atributos')
        print(f'Força: {self._character.attributes.power}')
        print(f'Destreza: {self._character.attributes.dexterity}')
        print(f'Constituição: {self._character.attributes.constitution}')
        print(f'Inteligência: {self._character.attributes.intelligence}')
        print(f'Sabedoria: {self._character.attributes.wisdom}')
        print(f'Carisma: {self._character.attributes.charisma}')


        print()
        print(f'# Raça')
        print(f'Nome: {self._character.race.name}')
        print(f'Movimento: {self._character.race.movement}m')
        print(f'Infrvisão: {self._character.race.infravision}m')
        print(f'Alinhamento: {self._character.race.alignment}')


        print()
        print(f'# Classe')
        print(f'Nome: {self._character.rpg_class.name}')
        print(f'Armas: {self._character.rpg_class.weapons}')
        print(f'Armaduras: {self._character.rpg_class.armors}')
        print(f'Itens mágicos: {self._character.rpg_class.magic_items}')
