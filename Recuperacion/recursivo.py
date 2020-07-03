import sys
from typing import *
from time import time


def subconjunto(x, y):
    def B(i, j):
        ultimo_i = i
        ultimo_j = j
        if i ==0 or j == 0:
            return 0
        #if (i, j) not in mem:

        if x[i-1] != y[j-1]:
            c1= B(i - 1, j)
            #print("c1",c1)
            c2=B(i, j - 1)
            #print("c2: ",c2)
            if c1>c2:
                mem[(i, j)] =[i-1, j]
                return c1

            else:
                mem[(i, j)] =[i, j-1]
                return c2

            #mem[(i,j)] = [max(c1[0],c2[0]),[i,j]]
            #return mem[(i,j)][0]

        if x[i-1] == y[j-1]:
            b = B(i - 1, j - 1)

            mem[(i,j)]=[i-1,j-1]
            return b+1
        #print( mem[i - 1, j - 1][0]," final")
        return mem[i-1, j-1][0]

    mem = {}
   # w = B(len(x), len(y))
    solution= B(len(x), len(y))
    print("solucion: ",solution)
    sol = []

    (i, j) = (len(x), len(y))
    while (i, j) in mem:
        # while historico[i][j] != None:
        #if mem[i, j] == (i - 1, j - 1):
        sol.append(i - 1)
        (i, j) = mem[i, j]

       # q, n = qPrev, nPrev
    sol.reverse()
    print(sol)
    return solution,sol



def leer_fichero(fichero: str):
    file = open(fichero)
    total = file.readline().strip()
    L = []
    for l in file:
        L.append(int(l.strip()))

    print(total, L)
    return total, L


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        start_time = time()  # Obtenemos el tiempo de inicio

        filename = sys.argv[1]
        N, L = leer_fichero(filename)
        minimo = min(L)
        maximo = max(L)
        eliminado = []

        comprobar = sorted(L)  # ordenamos de menor a mayor

        t = subconjunto(L, comprobar)
        print("T",t)
        elapsed_time = time() - start_time  # Calculamos el tiempo de ejecucion


        print("\nElapsed time: %.10f seconds." % elapsed_time)
