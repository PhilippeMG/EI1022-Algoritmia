import sys
from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *
from algoritmia.datastructures.mergefindsets import MergeFindSet
import random

from algoritmia.datastructures.queues import Fifo

from Utils.labyrinthviewer import LabyrinthViewer

Vertex = TypeVar("Vertex")
Edge = Wall = Tuple[Vertex, Vertex]


def get_edges(rows: int, cols: int, vertices_walls: str) -> List[Edge]: #obtener aristas
    # _Paso 1
    vertices = [(r, c) for r in range(rows) for c in range(cols)]

    # _Paso 3
    edges = []
    for (r, c) in vertices:  # la tupla (r, c) determina la posición del vértice.
        # La lista contiene para cada vertice
        if 'e' not in vertices_walls[r][c] and c + 1 < cols:  # No hay pared en el este y no es la última columna --> arista
            edges.append(((r, c), (r, c + 1)))

        if 's' not in vertices_walls[r][c] and r + 1 < rows:  # No hay pared en el sur y no es la última fila --> arista
            edges.append(((r, c), (r + 1, c)))

    return edges


def get_walls(rows: int, cols: int, vertices_walls: str) -> List[Wall]:  #obtener paredes

    vertices = [(r,c) for r in range(rows) for c in range(cols)]
    walls = []
    for (r,c) in vertices: # la tupla (r, c) determina la posición del vértice.
        if 'e' in vertices_walls[r][c] and c+1 < cols:
            walls.append( ((r, c), (r, c + 1)) )

        if 's' in vertices_walls[r][c] and r+1 < rows:
            walls.append( ((r, c),(r + 1, c)) )

    return walls


def create_labyrinth(rows: int, cols: int, vertices_walls: str) -> UndirectedGraph:
    edges = get_edges(rows, cols, vertices_walls)
    return UndirectedGraph(E=edges)

def create_labyrinth_without_wall(lab,arista):
    edges = list(lab.E)
    edges.append(arista)
    return UndirectedGraph(E=edges)


def recorredor_aristas_anchura(g: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    edges = []
    seen = set()
    queue = Fifo()

    seen.add(v_inicial)
    queue.push( (v_inicial,v_inicial) )

    while len(queue) > 0:
        u, v = queue.pop()
        edges.append( (u,v) )
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push( (v,suc) )

    return edges

def calcula_saltos(g: UndirectedGraph, v_inicial: Vertex):
    edges = recorredor_aristas_anchura(g, v_inicial)
    dic = {}
    dic[v_inicial] = 0
    for (u,v) in edges:
        if u != v:
            dic[v] = dic[u] + 1

    return dic

def get_edge_to_add(lab: UndirectedGraph, list_walls: List[Wall], v_treasure: Vertex, v_bomb: Vertex):
    dic_treasure = calcula_saltos(lab,v_treasure) #recorrido en anchura + -
    dic_bomb = calcula_saltos(lab, v_bomb)


    set_minimum = False

    for wall in list_walls:
        min_bomb = min(dic_bomb[(wall[0])], dic_bomb[(wall[1])])
        min_treasure = min(dic_treasure[(wall[0])], dic_treasure[(wall[1])])

        sum = min_treasure + min_bomb

        if not set_minimum:
            set_minimum=True
            minimum = sum
            edge = ( wall[0], wall[1] )

        if  sum < minimum :
            minimum = sum
            edge = ( wall[0], wall[1] )

    return edge


def get_path(lista_aristas: List[Edge], v_final: Vertex) -> List[Vertex]:
    #Paso 1. Construir diccionario de backpointers con lista_aristas
    bp = {}
    for (u, v) in lista_aristas:
        bp[v] = u


    #Paso 2. Recuperar el camino (saltos hacia atrás)
    v = v_final
    camino = [v]
    while v != bp[v]:
        v = bp[v]
        camino.append(v)

    camino.reverse()
    return camino



def load_labyrinth(filename: str) -> Tuple[Vertex, Vertex, int, int, UndirectedGraph]:
    text_file = open(filename)

    v_pos_tesoro = text_file.readline().rstrip().split(" ")
    pos_tesoro = (int(v_pos_tesoro[0]),int(v_pos_tesoro[1]))
    #print(pos_tesoro)

    v_pos_bomba = text_file.readline().rstrip().split(" ")
    pos_bomba = (int(v_pos_bomba[0]),int(v_pos_bomba[1]))
    #print(pos_bomba)

    v_tam_lab = text_file.readline().rstrip().split(" ")
    rows = int(v_tam_lab[0])
    cols = int(v_tam_lab[1])

    #print(rows,cols)

    vertices_walls = []
    for line in text_file:
        vertices_walls.append(line.rstrip().split(","))

    # Creamos el laberinto
    lab = create_labyrinth(rows, cols, vertices_walls)


    celda_entrada = (0, 0)
    celda_salida = (rows - 1, cols - 1)

    # Camino de celda inicio a celda tesoro
    aristas_desde_inicio = recorredor_aristas_anchura(lab, celda_entrada)
    camino_de_inicio_a_tesoro = get_path(aristas_desde_inicio, pos_tesoro)

    # Camino de celda tesoro a celda fin
    aristas_desde_tesoro = recorredor_aristas_anchura(lab, pos_tesoro)
    camino_de_tesoro_a_fin = get_path(aristas_desde_tesoro, celda_salida)

    # Logitud del camino pasando por el tesoro (sin bomba)
    camino_tesoro = camino_de_inicio_a_tesoro + camino_de_tesoro_a_fin # LO QUE HAY QUE DEVOLVER
    #print("Coste camino tesoro: ",camino_tesoro)


    # Camino de celda inicio a celda bomba
    camino_de_inicio_a_bomba = get_path(aristas_desde_inicio, pos_bomba)

    # Buscar pared a quitar
    walls = get_walls(rows,cols,vertices_walls)
    arista = get_edge_to_add(lab, walls, pos_tesoro, pos_bomba) # LO QUE HAY QUE DEVOLVER
    #print("Arista que eliminamos: ", arista)
    lab_sin_pared = create_labyrinth_without_wall(lab, arista)

    # Camino de celda bomba a celda tesoro
    aristas_desde_bomba = recorredor_aristas_anchura(lab_sin_pared, pos_bomba)
    camino_de_bomba_a_tesoro = get_path(aristas_desde_bomba, pos_tesoro)

    # Logitud del camino pasando por el tesoro (con bomba)
    camino_tesoro_bomba = camino_de_inicio_a_bomba + camino_de_bomba_a_tesoro + camino_de_tesoro_a_fin # LO QUE HAY QUE DEVOLVER
    #print("Coste camino tesoro con bomba: ",camino_tesoro_bomba)

    edge = arista[0]
    edge2 = arista[1]
    print(edge[0], edge[1], edge2[0], edge2[1])
    print(len(camino_tesoro)-2)
    print(len(camino_tesoro_bomba)-3)
    if len(sys.argv)==3 and sys.argv[2]=="-g":
        paint_labyrinth(lab_sin_pared,arista,camino_tesoro,camino_tesoro_bomba,pos_bomba,pos_tesoro)


    return (arista, camino_tesoro,camino_tesoro_bomba)

def paint_labyrinth(lab_sin_pared,arista,camino_tesoro,camino_tesoro_bomba,pos_bomba,pos_tesoro):

    viewer_lab = LabyrinthViewer(lab_sin_pared, canvas_width=1800, canvas_height=900, margin=10)

    viewer_lab.add_marked_cell(arista[0], "red", fillCell=True)
    viewer_lab.add_marked_cell(arista[1], "red", fillCell=True)
    viewer_lab.add_path(camino_tesoro, "lime", -2)
    viewer_lab.add_path(camino_tesoro_bomba, "blue", 2)
    viewer_lab.add_marked_cell(pos_bomba, "silver")
    viewer_lab.add_marked_cell(pos_tesoro, "yellow")

    viewer_lab.run()

if __name__ == '__main__':
    if not 2>len(sys.argv)>3:
        resultado =load_labyrinth(sys.argv[1])
    # arista=resultado[0]
    # edge=arista[0]
    # edge2=arista[1]
    # print(edge[0],edge[1],edge2[0],edge2[1])
    # print(resultado[1])
    # print(resultado[2])









