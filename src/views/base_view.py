
from abc import abstractmethod
from typing import TypeVar, override
from commom.helpers.console_helper import ConsoleHelper
from views.view import View

T = TypeVar('T')

class BaseView(View[T]):

    def __init__(self):
        self._console_helper: ConsoleHelper = ConsoleHelper()
        self._output: T | None = None


    @override
    def show(self):
        self._console_helper.clear_console()

        self.on_show()


    @override
    def get_output(self) -> T | None:
        return self._output


    @abstractmethod
    def on_show(self):
        pass
