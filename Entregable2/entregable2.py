
import sys
from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.prioritymaps import heapmap

from Utils.graphcoloring2dviewer import GraphColoring2DViewer

Vertex = TypeVar("Vertex")
Edge = Tuple[Vertex, Vertex]

# maybe we colud use this method...
def colour_vertex(lista: List[Vertex]) -> List[Set[int]]:
    res = []
    while len(lista) > 0:
        grupo = set()
        for v in lista:
            if all(v not in g.succs(u) for u in grupo):
                grupo.add(v)
        for elem in grupo:
            lista.remove(elem)
        res.append(grupo)

    return res


def algoritmo1(g: UndirectedGraph) ->Tuple[int, Dict[Tuple[int,int], int]]:
    # # List of vertices
    #------------------------------------------
    # vertices = set(g.V)
    # # Creating dictionary
    # dic = {}
    # for vertex in vertices:
    #     # Adding successors in dictionary
    #     dic[vertex] = len(g.succs(vertex))
    #------------------------------------------
    dic= crear_diccionario(g)
    # Sorting dictionary
    dic = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # Create list of sorted vertices
    lista_vertices = []
    for tupla in dic:
        vertex = tupla[0]
        lista_vertices.append(vertex)

    # Colour vertices
    grupos_vertices = colour_vertex(lista_vertices)

    # to understand
    num_used_colors = grupos_vertices

    #For each vertex we asign a color depending on its group
    diccionario_soluciones = {}
    for i, grupo in enumerate(grupos_vertices):
        for elem in grupo:
            diccionario_soluciones[elem] = i

    # Sort coloured vertices
    lista_ordenada = sorted(diccionario_soluciones.items())
    diccionario_ordenado = {}
    # Creation sorted dictionary of coloured vertices
    for (k, v) in lista_ordenada:
        #print(k[0], k[1], v)
        diccionario_ordenado[k] = v

    return [len(num_used_colors), diccionario_ordenado]

def algoritmo2(g: UndirectedGraph):  # ->Tuple[int, Dict[Tuple[int,int], int]]:
    #diccionario de prioridad heapsmaps
    # Creating dictionary
    dic =  crear_diccionario(g)
    heap=heapmap(dic)

    print(heap)

def crear_diccionario(g: UndirectedGraph):
    dic = {}
    vertices = set(g.V)

    for vertex in vertices:
        # Adding successors in dictionary
        dic[vertex] = len(g.succs(vertex))

    return  dic

# Creamos un grafo leyendo un fichero
def crear_grafo(filename: str) -> UndirectedGraph:
    text_file = open(filename)
    aristas = []
    for line in text_file:
        datos = line.rstrip().split(" ")  # vector 4 elementos

        aristas.append(((int(datos[0]), int(datos[1])), (int(datos[2]), int(datos[3]))))
    text_file.close()

    return UndirectedGraph(E=aristas)

def es_coloreado_correcto(g: UndirectedGraph, color_dic: Dict[Tuple[int, int], int]) -> bool:

    if len(color_dic) != len(g.V):
        return False

    for (u, v) in g.E:
        if color_dic[u] == color_dic[v]:
            return False
    return True

def imprimir_resultado(tupla: Tuple[int, Dict[Tuple[int,int], int]]):
    num_colores=tupla[0]
    dic = tupla[1]

    print (num_colores)
    for (k, v) in dic.items():
         print (k[0],k[1], v)


if __name__ == '__main__':
    # prgograma -1/-2 g

    if 1 < len(sys.argv) < 5:
        fichero = sys.argv[2]
        g = crear_grafo(fichero)

        tupla = []
        if (sys.argv[1]) == "-1":
            tupla = algoritmo1(g)


        elif (sys.argv[1]) == "-2":
            #tupla =
            algoritmo2(g)
            print("Algoritmo 2:\n {0}".format(tupla))
        #imprimimos resultados
       # num_colores = tupla[0]
       # dic = tupla[1]
       #
       #  print(num_colores)
       #  for (k, v) in dic.items():
       #      print(k[0], k[1], v)

        if len(sys.argv) == 4 and sys.argv[3] == "-g":
            # color_dic = {(-3, -2): 0, (0, 0): 1, (1, 1): 2}
            viewer = GraphColoring2DViewer(g, tupla[1], window_size=(800, 800))
            #  viewer = Graph2dViewer(g, window_size=(400, 200))
            viewer.run()

    else:
        print("ERROR: Incorrect parameters.")
