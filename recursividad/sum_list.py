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
        print(f'La suma total de la lista es: {total_sum}')
        return total_sum
        
    def printList(self):
        current = self.__first
        list = []
        print('Print list')
        while current is not None:
            list.append(current.data)
            current = current.next
        print(list)

