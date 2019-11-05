from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
#from Problemas.Sesion1y2_Graphs.problemas01 import create_labyrinth
from algoritmia.datastructures.queues import Fifo

from Utils.labyrinthviewer import LabyrinthViewer

from typing import *
import random
Vertex= TypeVar("Vertex")
Edge= Tuple[Vertex,Vertex]
def create_labyrinth(rows: int , cols: int,num: int) -> UndirectedGraph:
    #paso 1
    vertices= [(r,c) for r in range(rows) for c in range(cols)]

    #paso 2
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)

    #paso 3
    edges=[]
    for[r,c] in vertices:
        if c+1<cols:
            edges.append(((r,c),(r,c+1)))
        if r+1<rows:
            edges.append(((r,c),(r+1,c)))
    random.shuffle(edges)

    #paso4
    corridors=[]
    #paso5
    for (u,v) in edges:
        if mfs.find(u) != mfs.find(v):
            corridors.append((u,v))
            mfs.merge(u,v)
        elif num==0:
            mfs.append(u,v)
            num -= 1


    #paso6
    return UndirectedGraph(E=corridors)

def recorredor_aristas_profundidad(grafo: UndirectedGraph , v_inicial: Vertex)-> List[Edge]:
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in grafo.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)
            #aristas.append((u,v))
    aristas= []
    seen= set()
    recorrido_desde(v_inicial, v_inicial)
    return aristas
def recuperador_camino(lista_aristas: List[Edge], v_final: Vertex) -> List[Vertex]:

    #paso 1, Construir diccionario de backpointers con lista_artistas
    bp={}
    for (u,v) in lista_aristas:
        bp[v]=u

    #paso 2, Recuperar camino (saltos hacia atras)
    v=v_final
    camino = []
    while v != bp[v]:
        v=bp[v]
        camino.append(v)

    #Paso 3, Invertir camino y devolverlo
    camino.reverse()
    return  camino
def shortest_path(g: UndirectedGraph,source: Vertex, target:Vertex) -> List[Vertex]:
     lista_aristas= recorredor_aristas_anchura(lab,source)
     return recuperador_camino(lista_aristas,target)

def recorredor_aristas_anchura(grafo: UndirectedGraph, v_inicial: Vertex) -> "List[Vertex]":
    aristas = []
    queue = Fifo()
    seen = set()

    queue.push( (v_inicial,v_inicial) )
    seen.add(v_inicial)

    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append( (u, v) )
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push( ( v,suc) )

    return aristas
if __name__ == '__main__':
    random.seed(42)
    rows=80
    cols=140
    num_paredes_quitadas=100
    lab = create_labyrinth(rows,cols,num_paredes_quitadas)

    viewer = LabyrinthViewer(lab)
    #camino 1
    source=(0,0)
    target = (rows-1,cols -1)
    lista_aristas= recorredor_aristas_profundidad(lab,source)
    camino_a_target= recuperador_camino(lista_aristas,target)
    viewer.add_path(camino_a_target,"red",2)

    #camino 2
    source = (0, 0)
    target = (rows - 1, cols -1)
    camino_bueno=shortest_path(lab,source,target)
    camino_malo=recorredor_aristas_profundidad(lab,source)
    camino_a_target= recuperador_camino(camino_malo,target)


    viewer.add_path(camino_bueno, "blue",2)
    viewer.add_path(camino_a_target, "red",-2)

    viewer.run()
