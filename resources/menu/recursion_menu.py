
import os
from recursividad.sum_list import LinkedList

class RecursionMenu:
    def __init__(self):
        self.__list_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'
    
    def create_list(self):
        os.system('clear')
        limitList = input('Inserte un número entero para el límite de la lista: ')
        self.__list_module = LinkedList()
        self.__list_module.insertByClient(int(limitList))
        os.system('clear')
        print('✅ The list has been created successfully\n\n')
        return
    
    def print_list(self):
        if(self.__list_module is None):
            os.system('clear')
            print(self.__empty_message)
            return None
        os.system('clear')
        self.__list_module.printList()

    def print_total_sum(self):
        if(self.__list_module is None):
            os.system('clear')
            print(self.__empty_message)
            return None
        os.system('clear')
        total_sum = self.__list_module.total_addition()
    
    def event_manager(self, option_selected: int):
        print('option_selected', option_selected)
        options_lists = {
            1: self.create_list,
            2: self.print_list,
            3: self.print_total_sum,
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event