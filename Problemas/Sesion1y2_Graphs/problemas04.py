from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from Utils.graph2dviewer import Graph2dViewer
from Utils.labyrinthviewer import Vertex


def horse_graph(rows,cols):
    #creo los vertices
    vertices = [(r,c) for r in range(rows) for c in range (cols)]

    # Creo las aristas
    edges = []
    for (r,c) in vertices:
        for (ir,ic) in [(2,1),(1,2),(2,-1),(1,-2)]:
            if r+ir<rows and 0<= c+ic <cols:
                edges.append(((r,c),(r+ir,c+ic)))


    #Creo el grafo y lo devuelvo
    return UndirectedGraph(V=vertices,E=edges)

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
if __name__=='__main__':
    g= horse_graph(2,10)
    l_vert= recorredor_aristas_anchura(g,(0,0))
    print(len(l_vert))
    viewer=Graph2dViewer(g,vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()
