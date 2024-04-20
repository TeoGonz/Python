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
                self.agregar(nodo.izq, d)
        else: 
            if (nodo.ld == None):
                nodo.ld = Nodo(d)
            else:
                self.agregar(nodo.ld, d)
    def agregando(self, d):
        self.agregar(self.raiz, d)
    """ END AGREGAR """

    """ INORDER """
    def inorder(self, nodo):
        if(nodo != None):
            self.inorder(nodo.li)
            print('Inorder: ', nodo.dato)
            self.inorder(nodo.ld)
    
    def inordeno(self, d):
        self.inorder(self.raiz)
    """ END INORDER """

    """ POSTORDER """
    def postorder(self, nodo):
        if(nodo != None):
            self.postorder(nodo.li)
            self.postorder(nodo.ld)
            print('Postorder: ', nodo.dato)
    
    def postordeno(self, d):
        self.postorder(self.raiz)
    """ END POSTORDER """

    """ PREORDER """
    def preorder(self, nodo):
        if(nodo != None):
            print('Preorder: ', nodo.dato)
            self.preorder(nodo.li)
            self.preorder(nodo.ld)
    
    def preordeno(self, d):
        self.preorder(self.raiz)
    """ END PREORDER """

    """ BUSCAR """
    def buscar(self, nodo, d):
        if(nodo is None):
            return None
        else:
            if(nodo.dato == d):
                return nodo
            else:
                if(d<nodo.dato):
                    return self.buscar(nodo.li)
                else:
                    return self.buscar(nodo.ld)

    def buscando(self, d):
        return self.buscar(self.raiz, d)
    """ END BUSCAR """

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
    print('Cómo desea imprimir el árbol?')
    print('1.- Inorder')
    print('2.- Preorder')
    print('3.- Postorder')
    print('4.- Buscando')
    print('5.- Salir')
    opc = int(input("Ingrese la opción: "))

    if(opc==1):
        ar.inordeno(ar.raiz)
    elif(opc==2):
        ar.preordeno(ar.raiz)
    elif(opc==3):
        ar.postordeno(ar.raiz)
    elif(opc==4):
        d = int(input('Ingrese el dato a buscar: '))
        p = ar.buscando(ar.raiz, d)
        if(p is None):
            print('El dato no existe')
        else:
            print('El dato existe')
    elif(opc==5):
        break

""" 
    TAREA
    1. Hacer un método que cuente los nodos hoja del arbol. - (Las ligas que abren en derecha)
    2. Contador Nodos interiores, - (Las ligas que abren en izquierda)
    3. se debe hacer en un archivo py en blanco con solo los dos métodos. - Replicando el menú de esta hoja
"""