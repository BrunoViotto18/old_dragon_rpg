
from typing import TypeVar
from views.view import View


T = TypeVar('T')


class MenuOption[T]:

    def __init__(self, title: str, view: View[T]):
        self.title = title
        self.view = view
