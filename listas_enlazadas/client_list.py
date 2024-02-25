from listas_enlazadas.double_list import DoubleList, Node

class ClientList:
    #   Implementación de la lista doblemente enlazada
    #   Inserción de datios: [Edad, Sexo: 1: Hombre, 2: Mujer]
    def double_linked_list():
        double_list = DoubleList()  # Creación de la lista
        num_people = input('Insert number of people you want to register: ')
        while int(num_people) > 0:
            age = input('Insert age: ')
            sex = input('Insert sex: ')
            double_list.insert_in_start(int(age), int(sex))
            num_people = int(num_people) - 1
        
        # double_list.print_all()
        double_list.print_age_average()
        return
    double_linked_list()