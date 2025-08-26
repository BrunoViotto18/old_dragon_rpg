
import os


class ConsoleHelper():

    def clear_console(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
