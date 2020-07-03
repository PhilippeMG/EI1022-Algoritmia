from typing import *
from random import random, seed

def mientras_quepa(W: List[int], C: int) -> List[int]:
    total=0
    solucion=[]
    pos=0
    for w in  W:
        if total+w<C:
            solucion.append(pos)
            total=w+total
        else:
            total=w
            pos+=1
            solucion.append(pos)
    return solucion


# raise NotImplementedError
def primero_que_quepa(W: List[int], C: int) -> List[int]:
    solucion=[]
    usados=[0]
    for w in  W:
        for i  in range(len(usados)):
            total=usados[i]
            if total+w<=C:
                solucion.append(i)
                usados[i]=w+total
                break
            if i==len(usados)-1:
                solucion.append(len(usados))
                usados.append(w)
    return solucion

def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    solucion=[-1]*len(W)
    usados=[0]
    indices_ordenados=sorted(range(len(W)), key=lambda i:-W[i])
    for ordenado in  indices_ordenados:
        w= W[ordenado]
        for i  in range(len(usados)):
            total=usados[i]
            if total+w<=C:
                solucion[ordenado]=i
                usados[i]=w+total
                break
            if i==len(usados)-1:
                solucion[ordenado]=(len(usados))
                usados.append(w)
    return solucion
def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    #seed(42)
    #W, C = [int(random()*1000)+1 for i in range(1000)], 1000
    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        try:
            sol = solve(W, C)
            print("-" * 40)
            print("Método:", solve.__name__)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")
if __name__ == "__main__":
    prueba_binpacking()