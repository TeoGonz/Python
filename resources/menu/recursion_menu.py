
from resources.os_resources import OsResources
from recursividad.sum_list import LinkedList

class RecursionMenu:
    def __init__(self):
        self.__list_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'
    
    def create_list(self):
        OsResources().clear_console()
        limitList = input('Inert integer number for the limit of the list: ')
        self.__list_module = LinkedList()
        self.__list_module.insertByClient(int(limitList))
        OsResources().clear_console()
        print('✅ The list has been created successfully\n\n')
        return
    
    def print_list(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        self.__list_module.printList()

    def print_total_sum(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        total_sum = self.__list_module.total_addition()
    
    def recursion_printList(self, mode: str):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        linkedList = self.__list_module.copyList()
        preparedList = linkedList.merge_sort(linkedList._LinkedList__first, mode)
        # linkedList = self.__list_module._LinkedList__copy
        # linkedList = self.__list_module.merge_sort(linkedList, mode)
        linkedList.recursion_printList(preparedList)

    def asc_printList(self):
        self.recursion_printList('asc')
    
    def dsc_printList(self):
        self.recursion_printList('dsc')
    
    def event_manager(self, option_selected: int):
        print('option_selected', option_selected)
        options_lists = {
            1: self.create_list,
            2: self.print_list,
            3: self.print_total_sum,
            4: self.asc_printList,
            5: self.dsc_printList
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event