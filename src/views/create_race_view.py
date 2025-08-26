
from typing import override
from models.races.dwarf_race import DwarfRace
from models.races.elf_race import ElfRace
from models.races.halfling_race import HalflingRace
from models.races.human_race import HumanRace
from models.races.race import Race
from views.base_view import BaseView


class CreateRaceView(BaseView[Race]):

    def __init__(self):
        super().__init__()


    @override
    def on_show(self):
        print('Raças')
        print('[ 1 ] Humano')
        print('[ 2 ] Elfo')
        print('[ 3 ] Anão')
        print('[ 4 ] Halfling')
        option = int(input('Selecione a raça desejada: '))

        if option == 1:
            self._output = HumanRace()
        if option == 2:
            self._output = ElfRace()
        if option == 3:
            self._output = DwarfRace()
        if option == 4:
            self._output = HalflingRace()
