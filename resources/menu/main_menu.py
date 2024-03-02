# coding=utf-8
from resources.os_resources import OsResources
from resources.menu.lists_menu import ListMenu
from resources.menu.recursion_menu import RecursionMenu

class MainMenu:
    def __init__(self):
        self.__lists_menu = ListMenu()
        self.__recursion_menu = RecursionMenu()
    
    def main_menu(self):
        OsResources().clear_console()
        print('🐍🐍 Welcome to main menu 🐍🐍')
        print('________________________________________\n')
        print('What do you want to do?')
        option_main = int(input(
                'Linked double list menu:   Presione [1]\n'
                'Recursion menu:            Presione [2]\n'
                'Exit the app:              Presione [3]\n'
            ))
        options_main = {
            1: self.lists_menu,
            2: self.recursion_menu,
            3: exit
        }
        OsResources().clear_console()
        options_main.get(option_main, exit)() 
    
    def lists_menu(self):
        print('\n\n') 
        print('Linked double list menu')
        print('________________________________\n')
        print('What do you want to do?\n')
        option_selected = int(input(
                'Create a double linked list:   press [1]\n'
                'Print all elements in list:    press [2]\n'
                'Print women age average:       press [3]\n'
                'Print men age average:         press [4]\n'
                'Return to main menu:           Press [5]\n'
            ))
        print('\n\n')

        if(option_selected == 5):
            return self.main_menu()

        event = self.__lists_menu.event_manager(option_selected)
        
        if(event is None):
            return self.lists_menu()
    
    def recursion_menu(self):
        print('\n\n') 
        print('Recursion menu')
        print('______________________\n')
        print('What do you want to do?\n')
        option_selected = int(input(
                'Create a list:         press [1]\n'
                'Create array list      press [2]\n'
                'Print list:            press [3]\n'
                'Print array:           press [4]\n'
                'Print total sum:       press [5]\n'
                'Print asc list:        press [6]\n'
                'Print dsc list:        press [7]\n'
                'Return to main menu:   Press [8]\n'
            ))
        print('\n\n')

        if(option_selected == 8):
            return self.main_menu()

        event = self.__recursion_menu.event_manager(option_selected)
        
        if(event is None):
            return self.recursion_menu()