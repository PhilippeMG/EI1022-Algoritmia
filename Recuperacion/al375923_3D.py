import sys
from typing import *
from time import time
def subsecuencia(x: List[int], y: List[int]):

    def subsequence():
        visitados = []
        for _in in range(1 + len(x)):
            visitados.append([0] * (1 + len(y)))
        historico = []
        for _in in range(1 + len(x)):
            historico.append([None] * (1 + len(y)))
        for j in range(1, len(y)+1):
            visitados[0][j] = 0
            for i in range(1, len(x)+1):
                if x[i-1] == y[j-1]: visitados[i][j], historico[i][j] = visitados[i-1][j-1] + 1, (i-1, j-1)
                elif visitados[i][j-1] > visitados[i-1][j]: visitados[i][j], historico[i][j] = visitados[i][j-1], (i,j-1)
                else: visitados[i][j], historico[i][j] = visitados[i-1][j], (i-1,j)
        solution=[]
        (i, j) = (len(x), len(y))
        while historico[i][j] != None:
            if historico[i][j] == (i-1,j-1):
                solution.append(i-1)
            (i, j) = historico[i][j]

        return solution[::-1] #Invertimos la lista para tener los indices ordenados

    return subsequence()


def leer_fichero(fichero: str):
    file = open(fichero)
    total=file.readline().strip()
    L=[]
    for l in file:
        L.append(int(l.strip()))

    #print(total,L)
    return total,L

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        #start_time = time() #Obtenemos el tiempo de inicio
        #start_time = time() #Obtenemos el tiempo de inicio

        filename = sys.argv[1]
        N,L=leer_fichero(filename)
        minimo=min(L)
        maximo=max(L)
        eliminado=[]
        #comprobar= sorted(list(set(L)))# quitamos repetidos y ordenamos de menor a mayor
        comprobar= sorted(L)# ordenamos de menor a mayor

        #print("Lista ordenada sin repetidos: ",comprobar)
        #print("Lista ordenada con repetidos: ",comprobar)

        a=subsecuencia(L,comprobar)
        #print("tamaño: ",subsecuencia(L,comprobar))
        #elapsed_time = time() - start_time #Calculamos el tiempo de ejecucion

        if a!= None:
            print(len(a))
            for e in a:
                print(e)
           # print("Longitud de la LCS {} ".format(a ))
        else:
            print("NO SOLUTION")
        #
        #
        #print("\nElapsed time: %.10f seconds." % elapsed_time)
