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
        if(d<nodo.dato):
            if(nodo.li == None):
                nodo.li = Nodo(d)
            else:
                self.agregar(nodo.li, d)
        else: 
            if (nodo.ld == None):
                nodo.ld = Nodo(d)
            else:
                self.agregar(nodo.ld, d)
    def agregando(self, d):
        self.agregar(self.raiz, d)
    """ END AGREGAR """

    """ CONTAR RAMAS (INTERIORES) """
    def contar_ramas(self, nodo):
        if nodo is None:
            return 0
        if nodo.li is None and nodo.ld is None:
            return 0
        return self.contar_ramas(nodo.li) + self.contar_ramas(nodo.ld) + (1 if nodo != self.raiz else 0)
    def contando_ramas(self, nodo):
        print('contando_ramas: ', self.contar_ramas(nodo))
    """ END CONTAR RAMAS (INTERIORES) """

    """ CONTAR HOJAS """
    def contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.li is None and nodo.ld is None:
            return 1
        return self.contar_hojas(nodo.li) + self.contar_hojas(nodo.ld)
    def contando_hojas(self, nodo):
        print('contar_hojas', self.contar_hojas(nodo))
    """ END CONTAR HOJAS """

d = int(input("Ingrese el valor de la raiz: "))
ar = Arbol(d)

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
    print('Que desea contar en el arbol?')
    print('1.- Hojas')
    print('2.- Interiores')
    print('3.- Salir')
    opc = int(input("Ingrese la opción: "))

    if(opc==1):
        ar.contando_hojas(ar.raiz)
    elif(opc==2):
        ar.contando_ramas(ar.raiz)
    elif(opc==3):
        break

