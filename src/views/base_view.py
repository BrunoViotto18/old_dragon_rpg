
from abc import abstractmethod
from typing import override
from commom.helpers.console_helper import ConsoleHelper
from views.view import View


class BaseView(View):

    def __init__(self):
        self._console_helper: ConsoleHelper = ConsoleHelper()


    @override
    def show(self):
        self._console_helper.clear_console()

        self.on_show()


    @abstractmethod
    def on_show(self):
        pass

