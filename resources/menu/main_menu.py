# coding=utf-8
import os
from resources.menu.lists_menu import ListMenu

class MainMenu:
    def __init__(self):
        self.__lists_menu = ListMenu()
    
    def main_menu(self):
        os.system('clear')
        print('🐍🐍 Bienvenido al menú principal 🐍🐍')
        print('________________________________________\n')
        print('¿Que desea revisar?')
        option_main = int(input(
                'Para ejecutar el código de listas dobles enlazadas:    Presione [1]\n'
                'Para salir de la aplicación:                           Presione [2]\n'
            ))
        options_main = {
            1: self.lists_menu,
            2: exit
        }
        os.system('clear')
        options_main.get(option_main, exit)() 
    
    def lists_menu(self): 
        print('Menú de listas dobles enlazadas')
        print('________________________________\n')
        print('¿Que desea hacer?\n')
        option_selected = int(input(
                'Create a double linked list:   press [1]\n'
                'Print all elements in list:    press [2]\n'
                'Print women age average:       press [3]\n'
                'Print men age average:         press [4]\n'
                'Exit the app:                  Press [5]\n'
            ))
        print('\n\n')

        if(option_selected == 5):
            return self.main_menu()

        event = self.__lists_menu.event_manager(option_selected)
        
        if(event is None):
            return self.lists_menu()