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
            if self.__first is None:
                self.insertIntoEmptyList(i + 1)
            else:
                self.insertAtEnd(i + 1)            
    
    def insertIntoEmptyList(self, element):
        newNode = Node(element)
        self.__first = newNode

    def insertAtBeginning(self, element):
        newNode = Node(element)
        newNode.next = self.__first
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
        
    def printList(self):
        current = self.__first
        list = []
        print('Print list')
        while current is not None:
            list.append(current.data)
            current = current.next
        print(list)
            
    def multiple3Sum(self):
        current = self.__first
        sum = 0
        while current is not None:
            if current.data % 3 == 0:
                sum = sum + current.data
            current = current.next
        print('multiple of 3 sum: ',sum)
    
    def average(self):
        current = self.__first
        average = 0
        sum = 0
        while current is not None:
            self.__len += 1
            sum = sum + current.data
            current = current.next
        average = sum / self.__len
        print('average: ', average)


s = LinkedList()
limitList = input('Inserte un número entero para el límite de la lista: ')
if limitList: 
    s.insertByClient(int(limitList))
    s.printList()
    s.multiple3Sum()
    s.average()
    s.printList()