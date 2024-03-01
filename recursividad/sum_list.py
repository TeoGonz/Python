import random

class Node: 
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.__first = None
        self.__len = 0
    
    def insertByClient(self, limit: int):
        for i in range(limit):            
            random_number = random.randint(1, 10)
            if self.__first is None:
                self.insertIntoEmptyList(random_number)
            else:
                self.insertAtEnd(random_number)   

    def copyList(self):
        copy_list = LinkedList()  # Creamos una nueva lista enlazada para la copia
        current = self.__first
        while current:
            copy_list.add_in_list(current.data)  # Agregamos cada elemento de la lista original a la copia
            current = current.next
        return copy_list

    def add_in_list(self, data):
        newNode = Node(data)
        if not self.__first:
            self.__first = newNode
        else:
            current = self.__first
            while current.next:
                current = current.next
            current.next = newNode

    def insertIntoEmptyList(self, element):
        newNode = Node(element)
        self.__first = newNode
    
    def insertAtEnd(self, element):
        if self.__first is None:
            newNode = Node(element)
            self.__first = newNode
        else:
            current = self.__first
            while current.next is not None:
                current = current.next
            newNode = Node(element)
            current.next = newNode

    def recursive_addition(self, node):
        if node is None:
            return 0
        else:
            return node.data + self.recursive_addition(node.next)
    
    def total_addition(self):
        total_sum = self.recursive_addition(self.__first)
        print(f'The total using recusrive addition is: {total_sum}')
        return total_sum

    # se encarga de dividir la lista en dos mitades
    def split_list(self, linkedList):
        if linkedList is None or linkedList.next is None:
            return linkedList
        else:
            slow = linkedList
            fast = linkedList.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return middle

    # implementa el algoritmo de ordenación "Merge Sort" recursivamente y merge dependiendo si es asc o dsc combina dos sublistas ordenadas
    def merge_sort(self, linkedList, mode: str):
        if linkedList is None or linkedList.next is None:
            return linkedList
        else:
            middle = self.split_list(linkedList)
            left = self.merge_sort(linkedList, mode)
            right = self.merge_sort(middle, mode)
            if mode == 'asc':
                return self.asc_merge(left, right)
            elif mode == 'dsc':
                return self.dsc_merge(left, right)
            else:
                print('Invalid mode')

    # Implementa la unión de la lista, para validar si es de mayor a menor o de menor a mayor    
    def asc_merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.data < right.data:
            left.next = self.asc_merge(left.next, right)
            return left
        else:
            right.next = self.asc_merge(left, right.next)
            return right
    
    def dsc_merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        elif left.data > right.data:
            left.next = self.dsc_merge(left.next, right)
            return left
        else:
            right.next = self.dsc_merge(left, right.next)
            return right

    # Luego, la función imprimir simplemente imprime los elementos de la lista enlazada después de que se hayan ordenado.
    def recursion_printList(self, nodo):
        if nodo is None:
            return
        print(nodo.data)
        self.recursion_printList(nodo.next)
    
    def printList(self):
        current = self.__first
        listArray = []
        print('Print list\n')
        while current is not None:
            listArray.append(current.data)
            current = current.next
        print(listArray)

