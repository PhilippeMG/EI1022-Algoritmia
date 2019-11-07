
import sys
from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.prioritymaps import MaxHeapMap

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
    dic= crear_diccionario(g)
    # Sorting dictionary
    lista_ordenada = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # Create list of sorted vertices
    lista_vertices = []
    for tupla in lista_ordenada:
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
        diccionario_ordenado[k] = v

    return [len(num_used_colors), diccionario_ordenado]

def algoritmo2(g: UndirectedGraph) ->Tuple[int, Dict[Tuple[int,int], int]]:

    #obtenemos una lista vertices
    lista_vertices = g.V
    #creamos el diccionario
    dic = {}
    for v in lista_vertices:
        dic[v] = (0,len(g.succs(v)))
    diccionario_prioridad = MaxHeapMap(dic)

    #rellenamos el diccionario con los colores
    diccionario_grupo_colores = {}
    while len(diccionario_prioridad) > 0:
        elem = diccionario_prioridad.extract_opt()
        added = False
        vecinos = g.succs(elem)
        for i in sorted(diccionario_grupo_colores.keys()):
            if all(u not in diccionario_grupo_colores.get(i) for u in vecinos):
                diccionario_grupo_colores.get(i).append(elem)
                added = True
                break
        #le añadimos otro color si no estan disponibles los demas
        if added == False:
            diccionario_grupo_colores[len(diccionario_grupo_colores.keys())] = [elem]

        #actualizamos la puntuacion
        for sucesor in vecinos:
            if sucesor in diccionario_prioridad.keys():
                diccionario_prioridad[sucesor] = (diccionario_prioridad[sucesor][0]+1, diccionario_prioridad[sucesor][1])

    #asignamo un color para cada vertice

    diccionario_soluciones = {}
    for color in diccionario_grupo_colores.keys():
        for elem in diccionario_grupo_colores[color]:
            diccionario_soluciones[elem] = color


    lista_ordenada = sorted(diccionario_soluciones.items())
    diccionario_ordenado = {}
    for (k, v) in lista_ordenada:
        diccionario_ordenado[k] = v
    return [len(diccionario_grupo_colores), diccionario_ordenado]


    #-----------------------------------------------------------------------------

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
def comparar_solucion(tupla: Tuple[int, Dict[Tuple[int,int], int]],filename):
    num_colores = tupla[0]
    dic = tupla[1]
    lista = []
    for elem in dic.items():
        lista.append(elem)
    text_file = open(filename)
    pos=0
    primero=True
    for line in text_file:
        datos = line.rstrip().split(" ")  # vector 4 elementos
        if primero:
            primero=False
            #print(num_colores, "==",datos[0] )
            if not num_colores==int(datos[0]):
                return False
        else:
            list=lista[pos]
            vertex=list[0]
            x=vertex[0]
            y=vertex[1]
            c=dic[vertex]

            pos+=1
            if( x != int(datos[0]) or y != int(datos[1]) or c != int(datos[2]) ):

                return False
    text_file.close()

    return True




if __name__ == '__main__':
    # prgograma -1/-2 g

    if 1 < len(sys.argv) < 5:
        fichero = sys.argv[2]
        g = crear_grafo(fichero)

        tupla = []
        if (sys.argv[1]) == "-1":
            tupla = algoritmo1(g)


        elif (sys.argv[1]) == "-2":
            tupla = algoritmo2(g)

        imprimir_resultado(tupla)

        #print("Comparamos Solucion: ",comparar_solucion(tupla,"./test/graph-iberia.sol1"))
        #print(es_coloreado_correcto(g,tupla[1]))
        if len(sys.argv) == 4 and sys.argv[3] == "-g":
            viewer = GraphColoring2DViewer(g, tupla[1], window_size=(1000, 1000))
            viewer.run()

    else:
        print("ERROR: Incorrect parameters.")
