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
        # Crea una matriz de adyacencia con ceros inicialmente
        self.matriz_adyacencia = [[0] * num_nodos for _ in range(num_nodos)]

    def agregar_arista(self, inicio, fin):
        # Agrega una arista desde un nodo de inicio a un nodo final en la matriz de adyacencia
        self.matriz_adyacencia[inicio][fin] = 1  # Marca la conexión como 1

    def imprimir_matriz_adyacencia(self):
        # Imprime la matriz de adyacencia del grafo
        print("Matriz de adyacencia:")
        for fila in self.matriz_adyacencia:
            print(fila)


# Ejemplo de uso para un grafo conectado con la estructura deseada
g = Grafo(3)  # Creamos un grafo con 3 nodos

# Agregamos las aristas para hacer el grafo conectado con la estructura deseada
g.agregar_arista(0, 1)  # Conexión unidireccional entre nodo 0 y nodo 1

g.agregar_arista(1, 0)  # Conexión unidireccional de nodo 1 a nodo 0
g.agregar_arista(1, 2)  # Conexión unidireccional de nodo 1 a nodo 2

g.agregar_arista(2, 0)  # Conexión unidireccional de nodo 2 a nodo 0

# Imprimimos la matriz de adyacencia
g.imprimir_matriz_adyacencia()