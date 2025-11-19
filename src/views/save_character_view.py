import json
import os
from typing import override
from models.characters.character import Character
from views.base_view import BaseView


class SaveCharacterView(BaseView[None]):
    def __init__(self, character: Character):
        super().__init__()
        self._character = character

    @override
    def on_show(self):
        save_character = SaveCharacterView.ask_user_boolean('Deseja salvar o personagem?')

        if not save_character:
            confirmation = SaveCharacterView.ask_user_boolean('O personagem será descartado! Tem certeza que deseja descartar o personagem?')

            if confirmation:
                print('O personagem foi descartado')
                return

        file_name = input('Digite o nome do arquivo para esse personagem (sem extensão): ')

        content = json.dumps(self._character.__dict__, default=lambda x: x.__dict__)

        directory_path = os.path.join('save', 'characters')
        os.makedirs(directory_path, exist_ok=True)

        file_path = os.path.join(directory_path, f"{file_name}.json")

        with open(file_path, 'w') as file:
            try:
                file.write(content)
                file.flush()
                print('O personagem foi salvo com sucesso!')
            except Exception as e:
                print('Ocorreu um erro ao salvar o personagem.', e.__str__())


    @staticmethod
    def ask_user_boolean(question: str) -> bool:
        response = input(f'{question} [S/n] ')

        return response.lower() == "s"
