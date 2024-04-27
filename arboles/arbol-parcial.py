""" 
    TAREA
    1. Hacer un método que cuente los nodos hoja del arbol. - (Las ligas que abren en derecha)
    2. Contador Nodos interiores, - (Las ligas que abren en izquierda)
    3. se debe hacer en un archivo py en blanco con solo los dos métodos. - Replicando el menú de esta hoja
"""

class Nodo:
    def __init__(self, d):
        self.dato = d
        self.li = None
        self.ld = None

class Arbol:
    def __init__(self, d):
        self.raiz = Nodo(d)

    """ AGREGAR """
    def agregar(self, nodo, d):
        if d > nodo.dato:
            if nodo.li is None:
                nodo.li = Nodo(d)
            else:
                self.agregar(nodo.li, d)
        elif d < nodo.dato:
            if nodo.ld is None:
                nodo.ld = Nodo(d)
            else:
                self.agregar(nodo.ld, d)
    def agregando(self, d):
        self.agregar(self.raiz, d)
    """ END AGREGAR """

    """ BUSCAR """
    def buscar(self, nodo, d):
        if(nodo is None):
            return None
        else:
            if(nodo.dato == d):
                return nodo
            else:
                if(d>nodo.dato):
                    return self.buscar(nodo.li, d)
                else:
                    return self.buscar(nodo.ld, d)

    def buscando(self, d):
        return self.buscar(self.raiz, d)
    """ END BUSCAR """

    """ RECORER DE MANERA DESCENDENTE """
    def inorder(self, nodo):
        if nodo:
            # Primero recorremos el árbol de manera descendente hacia la izquierda
            self.inorder(nodo.li)
            # Luego imprimimos el valor del nodo
            print(nodo.dato)
            # Por último, recorremos el árbol de manera descendente hacia la derecha
            self.inorder(nodo.ld)
    
    def recorriendo_desc(self, nodo):
        print('recorriendo cedulas...', self.inorder(nodo))
    """ END RECORER DE MANERA DESCENDENTE  """

d = int(input("Ingrese el valor de la raiz: "))
ar = Arbol(d)
searchArr = []

while True:
    print('---- MENU ----')
    print("1.- Agregar")
    print("2.- Salir")
    opc = int(input("Ingrese la opción: "))
    if(opc==1):
        d = int(input("Ingrese el valor: "))
        ar.agregando(d)
    elif(opc==2):
        break

while True:
    print('----------- MENU -----------')
    print('Que deseas hacer en el arbol?')
    print('1.- Buscar')
    print('2.- Mostrar cedula descendente')
    print('3.- Mostrar coincidencias de busqueda terminados en 5')
    print('4.- Salir')
    opc = int(input("Ingrese la opcion: "))

    if(opc==1):
        d = int(input('Ingrese La cedula a buscar: '))
        p = ar.buscando(d)
        if(p is None):
            print('[La cedula no existe]')
        else:
            print('[La cedula existe]', p.dato)
            num = p.dato
            if num % 10 == 5:
                if num not in searchArr:
                    searchArr.append(num)
    elif(opc==2):
        ar.recorriendo_desc(ar.raiz)
    elif(opc==3):
        print('Coincidencias terminadas en 5', searchArr)
    elif(opc==4):
        break