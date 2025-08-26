
from abc import abstractmethod
from typing import TypeVar, override
from views.base_view import BaseView
from views.menus.menu_option import MenuOption


T = TypeVar('T')


class MenuView(BaseView[T]):

    def __init__(self):
        super().__init__()


    @override
    def on_show(self):
        options = self.get_options()

        for index, option in enumerate(options):
            print(f'[ {index + 1} ] {option.title}')

        print('[ 0 ] Sair')

        option = int(input('Digite a opção desejada: '))

        if option == 0:
            return

        menu_option = options[option - 1]

        menu_option.view.show()
        self._output = menu_option.view.get_output()


    @abstractmethod
    def get_options(self) -> list[MenuOption[T]]:
        pass
