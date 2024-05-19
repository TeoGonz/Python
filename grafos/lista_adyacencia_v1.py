class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor dado
        self.valor = valor
        self.siguiente = None  # Inicialmente, el siguiente nodo está vacío


class ListaLigada:
    def __init__(self):
        # Inicializa una lista ligada vacía
        self.cabeza = None  # La cabeza de la lista ligada inicialmente está vacía

    def agregar_al_final(self, valor):
        # Agrega un nodo con el valor dado al final de la lista ligada
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si la lista no está vacía, recorre la lista hasta el último nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            # Agrega el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        # Imprime los valores de todos los nodos en la lista ligada
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")  # Imprime el valor del nodo seguido de una flecha
            actual = actual.siguiente
        print("None")  # Indica el final de la lista


class Grafo:
    def __init__(self, num_nodos):
        # Inicializa un grafo con un número específico de nodos
        self.num_nodos = num_nodos
        # Crea una lista de listas ligadas, donde cada lista ligada representa los nodos adyacentes a un nodo específico
        self.lista_adyacencia = [ListaLigada() for _ in range(num_nodos)]

    def agregar_arista(self, inicio, fin):
        # Agrega una arista entre dos nodos en el grafo
        self.lista_adyacencia[inicio].agregar_al_final(fin)  # Añade el nodo final a la lista de adyacencia del nodo de inicio

    def imprimir_lista_adyacencia(self):
        # Imprime la lista de adyacencia del grafo
        for i, lista in enumerate(self.lista_adyacencia):
            print(f"Nodo {i}: ", end="")
            lista.imprimir()  # Imprime la lista de adyacencia para cada nodo
            
    def obtener_matriz_adyacencia(self):
        # Inicializa una matriz de adyacencia llena de ceros
        matriz = [[0] * self.num_nodos for _ in range(self.num_nodos)]

        # Llena la matriz de adyacencia con los valores de la lista de adyacencia
        for i, lista in enumerate(self.lista_adyacencia):
            actual = lista.cabeza
            while actual:
                matriz[actual.valor][i] = 1
                actual = actual.siguiente

        # Retorna la matriz de adyacencia
        return matriz


# Ejemplo de uso para el grafo deseado
g = Grafo(4)  # Creamos un grafo con 4 nodos

# Agregamos las aristas para el grafo deseado
g.agregar_arista(0, 2)
g.agregar_arista(0, 3)
g.agregar_arista(0, 4)

g.agregar_arista(1, 3)
g.agregar_arista(1, 1)
g.agregar_arista(1, 4)

g.agregar_arista(2, 1)
g.agregar_arista(2, 2)
g.agregar_arista(2, 4)

g.agregar_arista(3, 1)
g.agregar_arista(3, 2)
g.agregar_arista(3, 3)

# Imprimimos la lista de adyacencia
print("Lista de adyacencia:")
g.imprimir_lista_adyacencia()

# Obtenemos la matriz de adyacencia
matriz_adyacencia = g.obtener_matriz_adyacencia()

# Imprimimos la matriz de adyacencia
for fila in matriz_adyacencia:
    print(fila)