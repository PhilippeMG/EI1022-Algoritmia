from typing import *
from random import random, seed

def mientras_quepa(W: List[int], C: int) -> List[int]:
    solution=[]
    ocupado=0
    nc=0
    for obj in W:
        if ocupado + obj<=C:    # if ocupado + obj >C
            ocupado += obj      #   nc+=1
        else:                   #   ocupado=0
            ocupado=obj         #ocupado+=obj
            nc+=1               #solution.append(obj)
        solution.append(nc)
    return solution

def primero_que_quepa(W: List[int], C: int) -> List[int]:
    solution=[]
    nc=[C]

    for obj in W :
        for i,espacio in enumerate(nc):
            if espacio-obj>=0:
                nc[i]=espacio-obj
                solution.append(i)
                break
        else:
            nc.append(C-obj)
            solution.append(len(nc)-1)

    return solution

def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    solution = [0]*len(W) # solution=W
    nc = [C]
    indices_ordenados=sorted(range(len(W)), key=lambda i:-W[i])

    for indice in indices_ordenados:
        for i, espacio in enumerate(nc):
            if espacio - W[indice] >= 0:
                nc[i] = espacio - W[indice]
                solution[indice]=i
                break
        else:
            nc.append(C - W[indice])
            solution[indice]=(len(nc) - 1)

    return solution

def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
