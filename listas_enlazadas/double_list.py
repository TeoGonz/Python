#   Creado el: 2021/03/21
import json
from resources.return_average import GetAverage


#   Clase Nodo para la lista doblemente enlazada
class Node: 
    def __init__(self, age = None, sex = None, ld = None, li = None):
        self.age = age
        self.sex = sex
        self.ld = ld # Siguiente
        self.li = li # Anterior

#   Clase para la lista doblemente enlazada
class DoubleList:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__len = 0
        self.__age_average = 0

    #   Insertar en el final de la lista
    def insert_in_end(self, age: int, sex: int):
        new_node = Node(age, sex)
        if self.__start is None:
            self.__start = new_node
            self.__end = new_node
        else:
            new_node.li = self.__end
            self.__end.ld = new_node
            self.__end = new_node

    #   Insertar en el inicio de la lista
    def insert_in_start(self, age: int, sex: int):
        new_node = Node(age, sex)
        if self.__start is None:
            self.__start = new_node
            self.__end = new_node
        else:
            new_node.ld = self.__start
            self.__start.li = new_node
            self.__start = new_node

    #   Imprimir desde el inicio de la lista
    def print_from_start(self):
        current_node = self.__start
        while current_node is not None:
            # print('Edad:', current_node.age, 'Sexo:', current_node)
            current_node = current_node.ld

    #   Imprimir desde el final de la lista
    def print_from_end(self):
        current_node = self.__end
        while current_node is not None:
            # print('Edad:', current_node.age, 'Sexo:', current_node)
            current_node = current_node.li

    #   Imprimir todos los elementos de la lista
    def print_all(self):
        current_node = self.__start
        list = []
        while current_node is not None:
            element = json.dumps({"age": current_node.age, "sex": current_node.sex})            
            list.append(element)
            current_node = current_node.ld
        print(list);

    #   Imprimir el promedio de edades
    def print_age_average(self):
        current_node = self.__start
        list = []
        while current_node is not None:
            list.append(current_node.age)
            current_node = current_node.ld
        average_resource = GetAverage(list)


