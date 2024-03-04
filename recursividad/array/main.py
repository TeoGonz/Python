from array_menu import ArrayMenu

class ArrayMain:
    def __init__(self):
        self.__array_menu = ArrayMenu()

    def array_menu(self):
        print('\n\n') 
        print('Array menu')
        print('______________________\n')
        print('What do you want to do?\n')
        option_selected = int(input(
                'Create an array:           press [1]\n'
                'Print array:               press [2]\n'
                'Print total sum:           press [3]\n'
                'Exit:                      Press [4]\n'
            ))
        print('\n\n')

        if(option_selected == 4):
            return exit()

        event = self.__array_menu.event_manager(option_selected)
        
        if(event is None):
            return self.array_menu()

ArrayMain().array_menu()