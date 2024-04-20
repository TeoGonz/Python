class Node: 
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.__first = None
        self.__len = 0
        
    def isEmpty(self):
        return self.__first is None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.isEmpty() is True or data <= self.__first.data): 
            newNode.next = self.__first
            self.__first = newNode
        else:
            current = self.__first
            while (current.next != None and current.next.data < data):
                current = current.next
            newNode.next = current.next
            current.next = newNode
    
    def is_number_in_list(self, number):
        current_node = self.__first
        while current_node:
            if current_node.data == number:
                return True
            current_node = current_node.next
        return False
        
    def printList(self):
        current = self.__first
        list = []
        print('Print list')
        while current is not None:
            list.append(current.data)
            current = current.next
        print(list)
    
    def returnListElements(self):
        current = self.__first
        list = []
        while current is not None:
            list.append(current.data)
            current = current.next
        return list