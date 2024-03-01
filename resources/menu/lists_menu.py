from resources.os_resources import OsResources
from listas_enlazadas.client_list import ClientList

class ListMenu:
    def __init__(self):
        self.__list_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'

    def create_linked_list(self):
        OsResources().clear_console()
        self.__list_module = ClientList() 
        self.__list_module.create_double_linked_list()
        OsResources().clear_console()
        print('✅ The list has been created successfully\n\n')
        return
    
    def print_all_double_linked_list(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        self.__list_module.print_all_double_linked_list()
    
    def print_women_age_average(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        self.__list_module.print_women_age_average()
    
    def print_men_age_average(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None            
        OsResources().clear_console()
        self.__list_module.print_men_age_average()
    
    def event_manager(self, option_selected: int):
        options_lists = {
            1: self.create_linked_list,
            2: self.print_all_double_linked_list,
            3: self.print_women_age_average,
            4: self.print_men_age_average,
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event