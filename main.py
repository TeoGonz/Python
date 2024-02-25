import sys
from listas_enlazadas.client_list import ClientList

class Main:
    def __init__(self):
        self.__list_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'

    def create_linked_list(self):
        self.__list_module = ClientList() 
        self.__list_module.create_double_linked_list()
        print('✅ The list has been created successfully\n\n')
        return self.print_lists_menu()
    
    def print_all_double_linked_list(self):
        if(self.__list_module is None):
            print(self.__empty_message)
            return self.print_lists_menu()
        self.__list_module.print_all_double_linked_list()
        return self.print_lists_menu()            
    
    def print_women_age_average(self):
        if(self.__list_module is None):
            print(self.__empty_message)
            return self.print_lists_menu()
        self.__list_module.print_women_age_average()
        return self.print_lists_menu()
    
    def print_men_age_average(self):
        if(self.__list_module is None):
            print(self.__empty_message)
            return self.print_lists_menu()
        self.__list_module.print_men_age_average()
        return self.print_lists_menu()
    
    def print_lists_menu(self):
        print('\n\n\n')
        print('Menú de listas dobles enlazadas')
        print('¿Que desea hacer?\n')
        option_lists = int(input(
                'Create a double linked list:   press [1]\n'
                'Print all elements in list:    press [2]\n'
                'Print women age average:       press [3]\n'
                'Print men age average:         press [4]\n'
                'Exit the app:                  Press [5]\n'
            ))
        print('\n\n\n')
        options_lists = {
            1: self.create_linked_list,
            2: self.print_all_double_linked_list,
            3: self.print_women_age_average,
            4: self.print_men_age_average,
            5: self.main
        }        
        options_lists.get(option_lists, self.print_lists_menu)() # Usando recursividad para volver a imprimir el menú

    def main(self):
        print('Bienvenido al menú')
        print('¿Que desea revisar?')
        option_main = int(input(
                'Para ejecutar el código de listas dobles enlazadas:    Presione [1]\n'
                'Para salir de la aplicación:                           Presione [2]\n'
            ))
        options_main = {
            1: self.print_lists_menu,
            2: exit
        }
        options_main.get(option_main, exit)() # Usando recursividad para volver a imprimir el menú

#   Ejecución del programa
Main().main()