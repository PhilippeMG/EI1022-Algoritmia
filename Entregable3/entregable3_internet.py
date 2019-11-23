import sys
from time import time
from typing import *
from Utils.bt_scheme import PartialSolution, Solution, BacktrackingSolver


def leer_fichero(f):
    for line in open(f, "r", encoding="utf-8"):
        yield line.split()


def valor_ini(letra, palabras) -> int:
    for p in palabras:
        if letra == p[0]:
            return 1

    return 0


def crypto_solve(palabras: list):
    class CryptoAPS(PartialSolution):
        def __init__(self, valores_letras: dict, num=()):
            self.valores_letras = valores_letras
            self.visto = len(self.valores_letras.keys())
            self.n = len(letras)
            self.num = num

        def is_solution(self) -> bool:
            return self.n == self.visto

        def get_solution(self) -> Solution:
            return dict(self.valores_letras)

        def successors(self) -> Iterable["CryptoAPS"]:
            if self.n > self.visto:
                l = letras[self.visto]
                aux_valores = dict(self.valores_letras)

                for i in range(valor_ini(l, palabras), 10):
                    if i not in self.num:
                        aux_valores[l] = i
                        if factible(orden_letras, aux_valores):
                            yield CryptoAPS(aux_valores, self.num + (i, ))

    num_letras = len(palabras[-1])
    letras = []
    orden_letras = []

    for i in range(1, num_letras + 1):
        col = []

        for palabra in palabras:
            if (i - 1) < len(palabra):
                letra = palabra[-i]
                col.append(letra)

                if letra not in letras:
                    letras.append(letra)

        orden_letras.append(col)

    initial_ps = CryptoAPS({})
    return BacktrackingSolver.solve(initial_ps)


def factible(lista_letras, dic) -> bool:
    valor = 0

    for letra in lista_letras:
        if set(letra).issubset(dic.keys()):
            suma = 0

            for l in letra[:-1]:
                suma += dic[l]

            suma += valor
            valor = suma // 10

            if suma % 10 != dic[letra[-1]]:
                return False

            if suma != dic[letra[-1]] and letra == lista_letras[-1]:
                return False
        else:
            return True

    return True


def imprimir_sol(solucion, problema):
    linea_problema = "+".join(problema[:-1]) + " = " + problema[-1] + " => "

    if len(solucion) == 1:
        sol = solucion[0]
        lista_valores = []

        for palabra in problema:
            string = ""

            for letra in palabra:
                string += str(sol[letra])
            lista_valores.append(string)

        linea_problema += "+".join(lista_valores[:-1]) + " = " + lista_valores[-1]
        print(linea_problema)
    else:
        print(linea_problema + str(len(solucion)) + " soluciones")


if __name__ == '__main__':
    start_time = time()

    if len(sys.argv) == 2:
        file = sys.argv[1]

        for problemas in leer_fichero(file):
            soluciones = list(crypto_solve(problemas))
            imprimir_sol(soluciones, problemas)

    elif len(sys.argv) > 2:
        problemas = sys.argv[1:]
        soluciones = list(crypto_solve(problemas))
        imprimir_sol(soluciones, problemas)

    else:
        print("ERROR: Incorrect num parameters.")

    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
