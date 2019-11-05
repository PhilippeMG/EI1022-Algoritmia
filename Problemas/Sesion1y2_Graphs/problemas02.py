from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Problemas.Sesion1y2_Graphs.problemas01 import create_labyrinth
from Utils.labyrinthviewer import LabyrinthViewer

from typing import *
import random
Vertex= TypeVar("Vertex")
Edge= Tuple[Vertex,Vertex]

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

if __name__ == '__main__':
    random.seed(21619)
    rows=100
    cols=100

    lab = create_labyrinth(rows,cols)
    viewer = LabyrinthViewer(lab)
    source=(0,0)
    target = (rows-1,cols -1)
    lista_aristas= recorredor_aristas_profundidad(lab,source)
    camino_a_target= recuperador_camino(lista_aristas,target)

    viewer.add_path(camino_a_target)
    viewer.run()
