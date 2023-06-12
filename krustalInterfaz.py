# Programa en Python para el algoritmo de Kruskal
# para encontrar el árbol de expansión mínima de un grafo
# conectado, no dirigido y ponderado.

import networkx as nx
import matplotlib.pyplot as plt

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
        graph = nx.DiGraph()
        nodos=[]
        for nodo in range(self.V):
            nodos.append((nodo+1,str(nodo+1)))
        graph.add_nodes_from(nodos)

        costoMinimo = 0
        aristas=[]
        print("Aristas en el árbol de expansión mínima construido:")
        for u, v, peso in resultado:
            costoMinimo += peso
            print("%d -- %d == %d" % (u+1, v+1, peso))
            aristas.append((u+1, v+1, peso))
        graph.add_weighted_edges_from(aristas)
        if not nx.is_directed_acyclic_graph(graph):
            print("The graph is not acyclic.")
        else:
            # Draw the graph with labels and weights
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
            labels = nx.get_node_attributes(graph, 'label')
            nx.draw_networkx_labels(graph, pos, labels, font_color='black')
            edge_labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels)
            # Show the graph
            plt.show()
        print("Árbol de expansión mínima:", costoMinimo)
        costoMinimo = 0
        return(nodos,aristas)

from tkinter import Tk, Label, Entry, Button, Frame, messagebox

class InterfazGrafica:
    def __init__(self):
        self.ventana = Tk()
        # self.ventana.attributes('-fullscreen', True)
        self.ventana.geometry("800x600")
        self.ventana.title("Algoritmo de Kruskal")
        
        self.frame = Frame(self.ventana)
        self.frame.pack()
        
        self.label_nodos = Label(self.frame, text="Ingrese el número de nodos del grafo:")
        self.label_nodos.pack()
        
        self.entry_nodos = Entry(self.frame)
        self.entry_nodos.pack()
        
        self.label_arista = Label(self.frame, text="Ingrese el número de arista del grafo:")
        self.label_arista.pack()
        
        self.entry_arista = Entry(self.frame)
        self.entry_arista.pack()

        self.button_siguiente = Button(self.frame, text="Siguiente", command=self.crear_tabla_aristas)
        self.button_siguiente.pack()
        
        self.aristas = []
        
    def crear_tabla_aristas(self):
        try:
            num_arista = int(self.entry_arista.get())
            
            if num_arista < 1:
                messagebox.showerror("Error", "El número de arista del grafo debe ser mayor a 0.")
                return
            
            # self.label_nodos.pack_forget()
            # self.entry_nodos.pack_forget()
            # self.label_arista.pack_forget()
            # self.entry_arista.pack_forget()
            self.button_siguiente.pack_forget()
            
            self.label_aristas = Label(self.frame, text="Ingrese las aristas del grafo:")
            self.label_aristas.pack()
            
            self.tabla_aristas = Frame(self.frame)
            self.tabla_aristas.pack()
            
            for i in range(num_arista):
                label_origen = Label(self.tabla_aristas, text="Origen:")
                label_origen.grid(row=i, column=0)
                
                entry_origen = Entry(self.tabla_aristas)
                entry_origen.grid(row=i, column=1)
                
                label_destino = Label(self.tabla_aristas, text="Destino:")
                label_destino.grid(row=i, column=2)
                
                entry_destino = Entry(self.tabla_aristas)
                entry_destino.grid(row=i, column=3)
                
                label_peso = Label(self.tabla_aristas, text="Peso:")
                label_peso.grid(row=i, column=4)
                
                entry_peso = Entry(self.tabla_aristas)
                entry_peso.grid(row=i, column=5)
                
                self.aristas.append((entry_origen, entry_destino, entry_peso))
            
            self.button_calcular = Button(self.frame, text="Calcular MST", command=self.calcular_mst)
            self.button_calcular.pack()
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
        
    def calcular_mst(self):
        self.aristas_ingresadas = []
        g = Grafo(int(self.entry_nodos.get()))
        for arista in self.aristas:
            origen = arista[0].get()
            destino = arista[1].get()
            peso = arista[2].get()
            
            if origen and destino and peso:
                self.aristas_ingresadas.append((int(origen), int(destino), int(peso)))
                g.agregarArista(int(origen), int(destino), int(peso))

        if not self.aristas_ingresadas:
            messagebox.showerror("Error", "No se han ingresado aristas.")
            return
        nodos,aristas=g.KruskalMST()
        graph = nx.DiGraph()
        graph.add_nodes_from(nodos)
        graph.add_weighted_edges_from(aristas)
        if not nx.is_directed_acyclic_graph(graph):
            print("The graph is not acyclic.")
        else:
            # Draw the graph with labels and weights
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
            labels = nx.get_node_attributes(graph, 'label')
            nx.draw_networkx_labels(graph, pos, labels, font_color='black')
            edge_labels = nx.get_edge_attributes(graph, 'weight')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels)
            # Show the graph
            plt.show()
        # Realizar el cálculo del MST con las aristas ingresadas
        # Puedes utilizar la lista self.aristas_ingresadas
        
        # Mostrar el resultado en una nueva ventana o en el mismo Tkinter
        # Puedes personalizar cómo deseas mostrar el resultado
        
    def iniciar(self):
        self.ventana.mainloop()

# interfaz = InterfazGrafica()
# interfaz.iniciar()

# Código del controlador
if __name__ == '__main__':
    #solicitar ingreso de datos
    interfaz = InterfazGrafica()
    interfaz.iniciar()
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
    
