# Configuración del entorno para ejecutar el Algoritmo de Kruskal

Este repositorio contiene un programa en Python que implementa el algoritmo de Kruskal para encontrar el árbol de expansión mínima de un grafo conectado, no dirigido y ponderado. A continuación, se describe cómo configurar el entorno para ejecutar el algoritmo.

## Requisitos previos

- Python: Es necesario tener instalado Python en tu sistema. Puedes descargar la última versión de Python desde el sitio web oficial: <https://www.python.org/downloads/>

## Pasos

1. **Instalar Python:** Descarga e instala la versión más reciente de Python para tu sistema operativo.

2. **Instalar las bibliotecas requeridas:** El algoritmo utiliza las siguientes bibliotecas: `tkinter`, `matplotlib` y `networkx`. Para instalarlas, puedes usar el administrador de paquetes `pip` de la siguiente manera:

   ```
   pip install tkinter matplotlib networkx
   ```

   ```
   #si no funciona el comando anterior probar
   py -m pip install tkinter matplotlib networkx
   ```

   Esto instalará las bibliotecas necesarias en tu entorno de Python.

3. **Ejecutar el archivo:** Una vez que hayas instalado las bibliotecas, puedes ejecutar el archivo `kruskal.py` en un entorno Python. Para ello, abre una terminal o línea de comandos, navega hasta el directorio donde se encuentra el archivo y ejecútalo con el siguiente comando:

   ```
   python kruskal.py
   ```

   Esto iniciará la interfaz gráfica donde puedes ingresar los datos del grafo y ejecutar el algoritmo de Kruskal.

## Uso del algoritmo de Kruskal en la vida real

El algoritmo de Kruskal es ampliamente utilizado en diversos campos, como:

- Redes de comunicación: Se utiliza para encontrar la mínima longitud de cables o conexiones necesarios para interconectar nodos en una red.
- Sistemas de navegación: Puede utilizarse para encontrar la ruta más corta para conectar diferentes ubicaciones en un sistema de navegación.
- Optimización de rutas: Ayuda a encontrar la ruta óptima para minimizar costos o tiempos en problemas de logística y transporte.
- Análisis de redes sociales: Puede aplicarse para identificar las conexiones más relevantes o influyentes dentro de una red social.

## Funcionamiento del algoritmo de Kruskal

El algoritmo de Kruskal sigue los siguientes pasos:

1. **Ordenar las aristas:** Ordena todas las aristas del grafo en orden no decreciente de sus pesos.

2. **Inicializar estructuras:** Inicializa una estructura para almacenar el árbol de expansión mínima resultante y otra para realizar conjuntos disjuntos.

3. **Recorrer las aristas:** Recorre cada arista en orden ascendente de peso.

4. **Comprobar ciclos:** Para cada arista, verifica si agregarla al árbol de expansión causa un ciclo. Esto se hace utilizando la técnica de conjuntos disjuntos y comprobando si los nodos de origen y destino de la arista están en conjuntos diferentes.

5. **Agregar al árbol de expansión:** Si agregar la arista no causa un ciclo, se agrega al árbol de expansión mínimo y se fusionan los conjuntos a los que pertenecen los nodos de origen y destino.

6. **Finalización:** Una vez que se han recorrido todas

 las aristas o se ha alcanzado el número máximo de aristas permitidas en el árbol de expansión mínimo, se finaliza el algoritmo.

7. **Resultado:** El resultado es el árbol de expansión mínimo, que consiste en un conjunto de aristas que conectan todos los nodos del grafo con el mínimo costo total.

Este algoritmo es eficiente y garantiza encontrar la solución óptima para el problema del árbol de expansión mínima en grafos ponderados no dirigidos y conexos.
