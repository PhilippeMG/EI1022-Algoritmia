from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

from Utils.labyrinthviewer import LabyrinthViewer
import  random

def create_labyrinth(rows: int , cols: int) -> UndirectedGraph:
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
    #paso6
    return UndirectedGraph(E=corridors)
if __name__ == '__main__':
    random.seed(42)
    lab = create_labyrinth(40,60)
    viewer = LabyrinthViewer(lab,canvas_width=640, canvas_height=400,margin=10)
    viewer.run()