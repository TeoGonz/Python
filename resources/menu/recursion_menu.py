
from resources.os_resources import OsResources
from recursividad.sum_list import LinkedList

class RecursionMenu:
    def __init__(self):
        self.__list_module = None
        self.__empty_message = '⚠️ The list is empty, please create a list first\n\n'
    
    def create_list(self):
        OsResources().clear_console()
        #limitList = input('Inert integer number for the limit of the list: ')
        self.__list_module = LinkedList()
        #self.__list_module.insertRandomByLimit(int(limitList))
        self.insertByClient()
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
        self.__list_module.total_addition()
    
    def recursion_printList(self, mode: str):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        linkedList = self.__list_module.copyList()
        
        if(mode == 'recursive_right'):
            return linkedList.recursion_printList(linkedList._LinkedList__first)
        elif(mode == 'recursive_left'):
            return linkedList.recursion_printList_left(linkedList._LinkedList__first)
        elif(mode == 'asc' or mode == 'dsc'):
            preparedList = linkedList.merge_sort(linkedList._LinkedList__first, mode)
            linkedList.recursion_printList(preparedList)

    def show_recursive_list_left(self):
        self.recursion_printList('recursive_left')
    
    def show_recursive_list(self):
        self.recursion_printList('recursive_right')
    
    def asc_printList(self):
        self.recursion_printList('asc')
    
    def dsc_printList(self):
        self.recursion_printList('dsc')

    def insertByClient(self):
        limit = input('Insert integer for the limit of list: ')
        for i in range(int(limit)):
            vector_number = input('Insert integer number: ')
            self.__list_module.insertByClient(vector_number)
    
    def event_manager(self, option_selected: int):
        print('option_selected', option_selected)
        options_lists = {
            1: self.create_list,
            2: self.print_list,
            3: self.print_total_sum,
            4: self.show_recursive_list,
            5: self.show_recursive_list_left,
            6: self.asc_printList,
            7: self.dsc_printList
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event