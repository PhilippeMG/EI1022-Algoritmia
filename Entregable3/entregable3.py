

from typing import *
from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution
import sys


def cryptoA_solver(words_list, word_solution):
    class CryptoAPS(PartialSolution):
        def __init__(self, non_used_digits, letters, dic_solution):
            self.non_used_digits = non_used_digits # ¿..?
            self.letters = letters # Letras del problema
            self.dic_solution # Clave: letra, Valor: número
            self.n = len(dic_solution)

            def is_solution(self) -> bool:
                return self.n == len(letters) # True si -> longitud dic == letras que contiene el problema

            def get_solution(self) -> Solution:
                pass

            def successors(self) -> Iterable["PartialSolution"]:
                pass


    initial_ps = CryptoAPS((), (), {})
    return BacktrackingSolver.solve(initial_ps)


if __name__ == '__main__':
    if 1 < len(sys.argv) == 2:
        # El parámetro es un fichero
        ...


    elif len(sys.argv) > 2:
        # Se recibe más de una parámetro. Los parámetros son el problema.
        ...

    else:
        print("ERROR: Incorrect parameters.")


    for sol in cryptoA_solver(words_list=..., word_solution=...):
        print(sol)