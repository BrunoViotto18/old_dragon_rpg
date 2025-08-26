
from abc import abstractmethod
from typing import override
from views.base_view import BaseView
from views.menus.menu_option import MenuOption


class MenuView(BaseView):

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


    @abstractmethod
    def get_options(self) -> list[MenuOption]:
        pass
