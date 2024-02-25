class Node: 
    def __init__(self, age = None, sex = None, ld = None, li = None):
        self.age = age
        self.sex = sex
        self.ld = ld
        self.li = li

class DoubleList:
    def __init__(self):
        self.__li = None
        self.__ld = None
        self.__len = 0
    
    def insertByClient(self, age, sex):
        if self.__li is None:
            return self.insertIntoEmptyList(age, sex)
        else:
            return self.insertAtEnd(age, sex)

    def insertIntoEmptyList(self, age, sex):
        newNode = Node(age, sex)
        self.__li = newNode

    def insertAtEnd(self, age, sex):
        current = self.__li
        newNode = Node(age, sex)
        newNode.ld = None
        while current.ld is not None:
            current = current.ld
        current.ld = newNode
        newNode.li = current
    
    def printList(self):
        """ current = self.__li
        list = [] """
        """ while current is not None:
            list.append([current.age, current.sex])
            current = current.ld """
        """ print(list) """


s = DoubleList()
for i in range(2):  
    age = input('Inserte la edad de la persona: ')
    sex = input('Inserte numero de sexo [1] hombre [2] mujer: ')
    s.insertByClient(int(age), int(sex))

""" s.printList() """

print('Self', s)
""" 
if limitList: 
    s.insertByClient(int(limitList))
    s.printList()
    s.multiple3Sum()
    s.average()
    s.printList() """

