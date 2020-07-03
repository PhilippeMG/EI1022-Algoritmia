from time import time
from random import seed, random

from Utils.bt_scheme import PartialSolutionWithOptimization, Solution, Iterable, State, Union, BacktrackingOptSolver, \
    Tuple, BacktrackingSolver, BacktrackingVCSolver, PartialSolution

import sys
from typing import *

def inversion_solve(N, Tdb, Bdb, Tbt, Bbt):

    class inversionPS(PartialSolution):
        def __init__(self,solution,mes, valor_actual): # IMPLEMENTAR: Añade los parámetros que tú consideres

            self.solution = solution
            self.valor_actual = valor_actual
            self.mes = mes
        def is_solution(self) -> bool: # IMPLEMENTAR
            return self.mes==N

        def get_solution(self) -> Solution: # IMPLEMENTAR
            if self.is_solution():
                return round(self.valor_actual,2),self.solution
        def successors(self) -> Iterable["inversionPS"]: # IMPLEMENTAR
            #global  c
            #c+=1
            if not self.is_solution() :

                yield inversionPS(self.solution+("A",),self.mes+1,self.valor_actual)
                posicion = self.mes
                precio = (self.valor_actual-Tdb[posicion])*Bdb[posicion]

                yield inversionPS(self.solution+("B",),self.mes+1,precio)
                if (self.mes+6)<=(N):
                    precio = (self.valor_actual-Tbt[self.mes])*Bbt[self.mes]
                    yield inversionPS(self.solution+("C",),self.mes+6,precio)




        def state(self) -> State: # IMPLEMENTAR
            return self.mes,self.valor_actual

        def f(self) -> Union[int, float]:           # IMPLEMENTAR
             return -self.valor_actual

    initialPS = inversionPS((),0,1)                #73 637 ,36 895, 36 334 IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS) #opt Elapsed time: 0.1773691177 seconds.
                                                #BS Elapsed time: 0.2988674641 seconds.
                                                #VC Elapsed time: 0.3413732052 seconds.




def leer_fichero(fichero: str):
    file = open(fichero)
    texto=[]
    for l in file:
        texto.append(l.strip())
    N = int(texto[0])
    Tdb =[]
    E = texto[1]
    for e in E.split():
        Tdb.append(float(e))

    Bdb = []
    for e in texto[2].split():
        Bdb.append(float(e))

    Tbt = []
    for e in texto[3].split():
        Tbt.append(float(e))

    Bbt = []
    for e in texto[4].split():
        Bbt.append(float(e))



    return N,Tdb,Bdb,Tbt,Bbt

# Programa principal ------------------------------------------
if __name__ == "__main__":



    if len(sys.argv) >= 2:

        filename = sys.argv[1]
        N, Tdb, Bdb, Tbt, Bbt = leer_fichero(filename);
        m=[]
        #c=0
        #s=0
        #start_time = time() #Obtenemos el tiempo de inicio

        for i in inversion_solve(N, Tdb, Bdb, Tbt, Bbt):
            m.append(i)
            #print (i)
            #s+=1
        #elapsed_time = time() - start_time #Calculamos el tiempo de ejecucion
        #print("Maximo: ",max(m))
        #print("Minimo: ",min(m))
        sol=max(m)
        precio=sol[0]
        desisiones=sol[1]
        print(precio)
        print(len(desisiones))
        for d in desisiones:
            print(d)
        #print("Iteraciones : ",c, " soluciones: ",s)
        #print("\nElapsed time: %.10f seconds." % elapsed_time)
