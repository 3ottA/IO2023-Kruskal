# Programa en Python para el algoritmo de Kruskal
# para encontrar el árbol de expansión mínima de un grafo
# conectado, no dirigido y ponderado.


# Clase que representa un grafo
class Grafo:
    
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
    
    # Función para agregar una arista al grafo
    def agregarArista(self, u, v, w):
        self.grafo.append([u-1, v-1, w])
    
    # Función auxiliar para encontrar el conjunto de un elemento i
    # (utiliza la técnica de compresión de ruta)
    def encontrar(self, padre, i):
        if padre[i] != i:
            # Reasignación del padre del nodo
            # al nodo raíz, ya que se necesita
            # la compresión de ruta
            padre[i] = self.encontrar(padre, padre[i])
        return padre[i]
    
    # Función que realiza la unión de dos conjuntos x e y
    # (utiliza unión por rango)
    def union(self, padre, rango, x, y):
        # Se adjunta el árbol de rango menor al
        # árbol de rango mayor (Unión por Rango)
        if rango[x] < rango[y]:
            padre[x] = y
        elif rango[x] > rango[y]:
            padre[y] = x
        else:
            padre[y] = x
            rango[x] += 1
    
    # La función principal para construir el árbol de expansión mínima
    # utilizando el algoritmo de Kruskal
    def KruskalMST(self):
        # Esto almacenará el árbol de expansión mínima resultante
        resultado = []
        
        # Una variable de índice, utilizada para las aristas ordenadas
        i = 0
        
        # Una variable de índice, utilizada para result[]
        e = 0
        
        # Ordenar todas las aristas en orden no decreciente de su peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        
        padre = []
        rango = []
        
        # Crear V subconjuntos con elementos individuales
        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)
        
        # El número de aristas que se tomarán es menor que V-1
        while e < self.V - 1:
            # Seleccionar la arista más pequeña y aumentar
            # el índice para la próxima iteración
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)
            
            # Si incluir esta arista no causa un ciclo,
            # entonces se incluye en el resultado y se
            # incrementa el índice del resultado para la próxima arista
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(padre, rango, x, y)
            # Si no, se descarta la arista
        
        costoMinimo = 0
        print("Aristas en el árbol de expansión mínima construido:")
        for u, v, peso in resultado:
            costoMinimo += peso
            print("%d -- %d == %d" % (u+1, v+1, peso))
        print("Árbol de expansión mínima:", costoMinimo)


# Código del controlador
if __name__ == '__main__':
    #solicitar ingreso de datos
   
    print("Ingrese el número de nodos del grafo:")
    n = int(input())
    g = Grafo(n)
    while True:
        if n < 1:
            print("El número de nodos del grafo debe ser mayor a 0")
            print("Ingrese el número de nodos del grafo:")
            n = int(input())
        print('Desea agregar arista? (y/n)')
        respuesta = input()
        if respuesta == 'n':
            break
        print("Ingrese el nodo de origen, el nodo de destino y el peso de la arista:")
        u = int(input('origen: '))
        v = int(input('destino: '))
        w = int(input('peso: '))
        g.agregarArista(u, v, w)

    g.KruskalMST()
    # g = Grafo(6)
    # g.agregarArista(1, 2, 7)
    # g.agregarArista(1, 3, 9)
    # g.agregarArista(1, 6, 14)
    # g.agregarArista(2, 3, 10)
    # g.agregarArista(2, 4, 5)
    # g.agregarArista(3, 4, 11)
    # g.agregarArista(4, 5, 6)
    # g.agregarArista(5, 6, 9)
    
