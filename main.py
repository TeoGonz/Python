import sys
from listas_enlazadas.lists_menu import ListMenu

class Main:
    def __init__(self):
        self.__lists_menu = ListMenu()

    def main(self):
        print('Bienvenido al menú')
        print('¿Que desea revisar?')
        option_main = int(input(
                'Para ejecutar el código de listas dobles enlazadas:    Presione [1]\n'
                'Para salir de la aplicación:                           Presione [2]\n'
            ))
        options_main = {
            1: self.__lists_menu.print_lists_menu,
            2: exit
        }
        options_main.get(option_main, exit)() # Usando recursividad para volver a imprimir el menú

#   Ejecución del programa
Main().main()