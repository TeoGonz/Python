from lista import LinkedList

class MainMenu:
    def __init__(self):
        self.list_one = LinkedList()
        self.list_two = LinkedList()
        self.list_three = LinkedList()
    
    def main_menu(self):
        print('\n\n')
        print('🐍🐍 Welcome to main menu 🐍🐍')
        print('________________________________________\n')
        print('What do you want to do?')
        print('1. Insert elements into the list one')
        print('2. Show elements into the list one')
        print('3. Insert elements into the list two')
        print('4. Show elements into the list two')
        print('5. Insert elements into the list three')
        print('0. Exit the app')
        option = int(input('Enter the option: '))
        self.event_manager(option)

    # MOSTRAR LISTAS
    def printList_one(self):
        self.list_one.printList()
        self.main_menu()

    def printList_two(self):
        self.list_two.printList()
        self.main_menu()

    # INSERT IN LIST ONE
    def insert_list_one(self):
        self.insert_data_in_list(self.list_one)
    
    # INSERT IN LIST TWO
    def insert_list_two(self):
        self.insert_data_in_list(self.list_two)
    
    # INSERT IN LIST THREE
    def insert_list_three(self):
        if(self.list_one.isEmpty() or self.list_two.isEmpty()):
            print('The lists are empty')
            self.main_menu()
        else:
            self.iterate_for_list_three(self.list_one)
            self.iterate_for_list_three(self.list_two)
            print('Lo que hay en lista uno', self.list_one.returnListElements())
            print('Lo que hay en lista dos', self.list_two.returnListElements())
            print('Lo que hay en lista tres', self.list_three.returnListElements())
            self.main_menu()
    
    # ESTE MÉTODO SE USA PARA INSERTAR DATA DE UNA LISTA A LA LISTA TRES
    def iterate_for_list_three(self, listParam: LinkedList):
        for i in listParam.returnListElements():
                valid = self.list_three.is_number_in_list(i)
                if(valid == False): self.list_three.insertAtEnd(i) 

    
    # PARA LAS LISTAS UNO Y DOS
    def insert_data_in_list(self, listParam: LinkedList):
        stop = 1
        while stop == 1:
            number = int(input('Enter the number: '))
            valid = listParam.is_number_in_list(number)
            if(valid): print('The number is already in the list')
            else: listParam.insertAtEnd(number)            
            stop = int(input('Do you want to continue?  Yes 1. No: 0 :   \n'))
        self.main_menu()
    
    def event_manager(self, option_selected: int):
        options_lists = {
            1: self.insert_list_one,
            2: self.printList_one,
            3: self.insert_list_two,
            4: self.printList_two,
            5: self.insert_list_three,
            0: exit
        }        
        event = options_lists.get(option_selected, None)() # Usando recursividad para volver a imprimir el menú
        return event

MainMenu().main_menu()