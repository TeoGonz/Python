import os

class OsResources: 
    def __init__(self):
        self.os = os

    def clear_console(self):
        print(os.name)
        if os.name == "posix":
            os.system('clear')
        elif os.name == "nt":
            os.system('cls')
        else:
            print('No os found')