import sys
from typing import *
from time import time

def prueba_distribucion(Ua,Ub,N,Ca,Cb,P):
    # Ua = 35 #Numero de componentes en el almacen
    # Ub = 47 #Numero de componentes en el almacen
    #
    # N = 4 #Numero de fabricas
    # Ca = [2,10,5,15] #Coste de enviar una unidad del almacen A a la fabrica i
    # Cb = [3,9,6,16]
    # P = [10,5,30,9] #Pi es el número de componentes que necesita la fábrica i.
    coste=0
    solucion=[(0,0)]*N
    #Devolveremos una lista de tuplas [(Ua,Ub),(Ua,Ub),(Ua,Ub),(Ua,Ub)]
    #for i in range(N):
    if (sum(Ca)>sum(Cb)):
        indices_ordenados = sorted(range(len(Ca)), key=lambda i: -(P[i]*Ca[i]))
        print(indices_ordenados)
    else:
        indices_ordenados = sorted(range(len(Ca)), key=lambda i: -(P[i]*Cb[i]))
        #print(indices_ordenados)


    #indices_ordenados=[1,2,0,3]
    for i in (indices_ordenados):
        envio=[0,0]
        if (Ca[i]<=Cb[i]):
            #print("Envia A")

            if(Ua>=P[i]):
                coste+=P[i]*Ca[i]
                envio=[P[i],0]
                Ua-=P[i]
            else:
                disponibles=P[i]-Ua
                #print(Ua," ",P[i])
                envio=[Ua,(disponibles)]
                Ub-=(disponibles)
                coste+=Ua*Ca[i]+(disponibles)*Cb[i]
                Ua=0

        else:
            #print("Envia B")
            if(Ub>=P[i]):
                coste+=P[i]*Cb[i]
                envio=[0,P[i]]
                Ub-=P[i]
            else:
                disponibles = P[i] - Ub
                envio=[(disponibles),Ub]
                Ua -= disponibles
                coste+=(Ub*Cb[i])+(disponibles*Ca[i])
                Ub = 0


        solucion[i]=envio
    #print("Restantes a: ",Ua," Restantes b: ", Ub)

    return (coste,solucion)


def leer_fichero(fichero: str):
    file = open(fichero)
    texto=[]
    for l in file:
        texto.append(l.strip())
    Ua = int(texto[0])
    Ub = int(texto[1])
    N = int(texto[2])

    Ca =[]

    for e in texto[3].split():
        Ca.append(int(e))

    Cb = []

    for e in texto[4].split():
        Cb.append(int(e))
    P = []

    for e in texto[5].split():
        P.append(int(e))



    return Ua,Ub,N,Ca,Cb,P

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        #start_time = time() #Obtenemos el tiempo de inicio
      #  start_time = time() #Obtenemos el tiempo de inicio

        filename = sys.argv[1]
        Ua,Ub,N,Ca,Cb,P=leer_fichero(filename)
        coste, solucion= prueba_distribucion(Ua,Ub,N,Ca,Cb,P)
      #  elapsed_time = time() - start_time #Calculamos el tiempo de ejecucion

        print(coste)
        for a,b in solucion:
            print(a,b)
      #  print("\nElapsed time: %.10f seconds." % elapsed_time)
