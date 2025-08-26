
from views.view import View


class MenuOption:

    def __init__(self, title: str, view: View):
        self.title = title
        self.view = view
