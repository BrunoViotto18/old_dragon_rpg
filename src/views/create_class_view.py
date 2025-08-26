
from typing import override
from models.classes.clergyman_class import ClergymanClass
from models.classes.mage_class import MageClass
from models.classes.rpg_class import RpgClass
from models.classes.warrior_class import WarriorClass
from views.base_view import BaseView


class CreateClassView(BaseView[RpgClass]):

    def __init__(self):
        super().__init__()


    @override
    def on_show(self):
        print('Raças')
        print('[ 1 ] Guerreiro')
        print('[ 2 ] Clérigo')
        print('[ 3 ] Mago')
        option = int(input('Selecione a class desejada: '))

        if option == 1:
            self._output = WarriorClass()
        if option == 2:
            self._output = ClergymanClass()
        if option == 3:
            self._output = MageClass()
