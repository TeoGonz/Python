#from resources.os_resources import OsResources
import os
from sum_array import SumArray

class ArrayMenu: 
    def __init__(self):
        self.__array_list = []
        self.__array_iterator = 0
        self.__sum_array_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'

    def create_array(self):
        self.clear_console()
        self.__sum_array_module = SumArray()
        limitArray = input('Insert integer number for the limit of the array: ')
        for i in range(int(limitArray)):
            vector_number = input('Insert integer number: ')
            self.__array_list = self.__sum_array_module.push(self.__array_list, int(vector_number))
        self.clear_console()
        print('✅ The array has been created successfully\n\n')
        return
    
    def print_array(self):
        if(len(self.__array_list) == 0):
            self.clear_console()
            print('⚠️ The array is empty, please create an array first\n\n')
            return None
        self.clear_console()
        print('ARRAY LIST : \n', self.__array_list)

    def print_total_sum_arr(self):
        self.clear_console()
        print('RECURSION ADDITION SUM ARRAY : \n\n', self.__sum_array_module.sum_array(self.__array_list, self.__array_iterator))
    
    def event_manager(self, option_selected: int):
        print('option_selected', option_selected)
        options_lists = {
            1: self.create_array,
            2: self.print_array,
            3: self.print_total_sum_arr,
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event
    
    def clear_console(self):
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        else:
            print('No os found')