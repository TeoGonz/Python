from listas_enlazadas.double_list import DoubleList, Node


#   Implementación de la lista doblemente enlazada
class ClientList:
    def __init__(self):
        self.__double_list = None
    #   Inserción de datios: [Edad, Sexo: 1: Hombre, 2: Mujer]
    def create_double_linked_list(self):
        self.__double_list = DoubleList()  # Creación de la lista
        num_people = input('Insert number of people you want to register: ')
        while int(num_people) > 0:
            age = input('Insert age: ')
            sex = input('Insert sex: ')
            self.__double_list.insert_in_start(int(age), int(sex))
            num_people = int(num_people) - 1
        return
    
    def print_all_double_linked_list(self):
        self.__double_list.print_all()
        return
    
    def print_women_age_average(self):
        self.__double_list.print_age_average_women()
        return
    
    def print_men_age_average(self):
        self.__double_list.print_age_average_men()
        return