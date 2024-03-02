
from resources.os_resources import OsResources
from recursividad.sum_list import LinkedList
from recursividad.sum_array import SumArray

class RecursionMenu:
    def __init__(self):
        self.__array_list = []
        self.__array_iterator = 0
        self.__list_module = None
        self.__sum_array_module = None
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
    
    def create_array(self):
        OsResources().clear_console()
        self.__sum_array_module = SumArray()
        limitArray = input('Insert integer number for the limit of the array: ')
        for i in range(int(limitArray)):
            vector_number = input('Insert integer number: ')
            self.__array_list = self.__sum_array_module.push(self.__array_list, int(vector_number))
        OsResources().clear_console()
        print('✅ The array has been created successfully\n\n')
        return
    
    def print_list(self):
        if(self.__list_module is None):
            OsResources().clear_console()
            print(self.__empty_message)
            return None
        OsResources().clear_console()
        self.__list_module.printList()

    def print_array(self):
        if(len(self.__array_list) == 0):
            OsResources().clear_console()
            print('⚠️ The array is empty, please create an array first\n\n')
            return None
        OsResources().clear_console()
        print('ARRAY LIST : ', self.__array_list)
        self.print_total_sum_arr()
    
    def print_total_sum_arr(self):
        print('RECURSION ADDITION SUM ARRAY : ', self.__sum_array_module.sum_array(self.__array_list, self.__array_iterator))

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
        preparedList = linkedList.merge_sort(linkedList._LinkedList__first, mode)
        # linkedList = self.__list_module._LinkedList__copy
        # linkedList = self.__list_module.merge_sort(linkedList, mode)
        linkedList.recursion_printList(preparedList)

    def asc_printList(self):
        self.recursion_printList('asc')
    
    def dsc_printList(self):
        self.recursion_printList('dsc')

    def insertByClient(self):
        limit = input('Insert integer for the limit of list: ')
        for i in range(int(limit)):
            vector_number = input('Insert integer number: ')
            #
            self.__list_module.insertByClient(vector_number)
    
    def event_manager(self, option_selected: int):
        print('option_selected', option_selected)
        options_lists = {
            1: self.create_list,
            2: self.create_array,
            3: self.print_list,
            4: self.print_array,
            5: self.print_total_sum,
            6: self.asc_printList,
            7: self.dsc_printList
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event