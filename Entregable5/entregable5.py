import sys
from time import time

def leer_fichero(fichero):
    #El fichero consta de 3 lineas en la primera tenemos la K(Tamaño maximo) C(Peso maximo) N(Numero de objetos)
    #La segunda linea del fichero es un vector de elementos que sera el valor
    #La tercera liena del fichero es un vector de elementos que sera el peso
    file = open(fichero, encoding='utf-8')
    datos = []
    for line in file:
        info = line.split()
        lista = []
        for elem in info:
            lista.append(int(elem))
        datos.append(lista)
    return datos

def mochila(K, C, N, V, P):
    def _mochila(n,c,k):
        if n == 0 and k == 0: return 0

        if n == 0 and k > 0: return -float("infinity")

        if (n, c, k) not in mem:
            v, p = V[n - 1], P[n - 1]  # Recorrido de n-1 a 0
            if p <= c and k > 0:
                mem[n, c, k] = max((_mochila(n - 1, c - p * d, k - d) + v * d, (n - 1, c - p * d, k - d), d) for d in (0, 1))
            else:
                mem[n, c, k] = (_mochila(n - 1, c, k), (n - 1, c, k), 0)

            return mem[n, c, k][0]

        return mem[n, c, k][0]
    mem = {}
    valor = _mochila(N,C,K)
    if valor == -float("infinity"):
        return "NO SOLUTION"
    n, c, k = N, C, K

    sol = []
    while n > 0 and k > 0:
        _, (n_previo, c_previo, k_previo), decision = mem[n,c,k]
        if decision == 1:
            sol.append(n_previo)
        n, c, k = n_previo, c_previo, k_previo

    sol.reverse()
    peso = C - c # Se resta a la capacidad la capacidad restante después de haber recorrido todos los elementos.

    return valor, peso, sol


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Obtenemos el tiempo de inicio
        start_time = time()

        filename = sys.argv[-1]
        datos_problema = leer_fichero(sys.argv[1])

        #Mostramos los datos leidos en una lista de enteros
        for dato in datos_problema:
            print(dato)

        #Llamamos al metodo dinamico
        print("\n----Resultado----\n")
        K, C, N = datos_problema[0] # Valores del problema
        V = datos_problema[1] # Vector de valores
        P = datos_problema[2] # Vector de pesos

        ans = mochila(K, C, N, V, P)

        if ans == "NO SOLUTION":
            print(ans)
        else:
            valor_mochila = ans[0]
            peso_mochila = ans[1]
            print(valor_mochila)
            print(peso_mochila)
            objects = ""
            for elem in ans[2]:
                objects += str(elem) + " "
            print(objects)
        #Calculamos el tiempo de ejecucion
        elapsed_time = time() - start_time
        print("\nElapsed time: %.10f seconds." % elapsed_time)

    else:
        print("Incorrect number of parameters.")