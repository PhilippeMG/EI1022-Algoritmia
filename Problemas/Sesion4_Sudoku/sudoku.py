from copy import deepcopy

from Utils.bt_scheme import PartialSolution, BacktrackingSolver
from typing import *

Position = Tuple[int, int]
Sudoku = List[List[int]]


def primera_vacia(s: Sudoku) -> Optional[Position]:
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                return fila, col
    return None  # si el Sudoku ya está completo
def vacias(s: Sudoku) -> Set[Position]:
    res=set()
    for fila in range(9):
        for col in range(9):
            if s[fila][col] == 0:
                res.add((fila, col))
    return res  # si el Sudoku ya está completo


def posibles_en(s: Sudoku, fila: int, col: int) -> Set[int]:
    used = set(s[fila][c] for c in range(9))
    used = used.union(s[f][col] for f in range(9))
    fc, cc = fila // 3 * 3, col // 3 * 3
    used = used.union(s[fc + f][cc + c] for f in range(3) for c in range(3))
    return set(range(1, 10)) - used


def pretty_print(s: Sudoku):
    for i, fila in enumerate(s):
        for j, columna in enumerate(fila):
            print(columna if columna != 0 else ' ', end="")
            if j in [2, 5]:
                print("|", end="")
        print()
        if i in [2, 5]:
            print("---+---+---")


class SudokuPS(PartialSolution):
    def __init__(self, sudoku: Sudoku,vacias):
        self.s = sudoku
        self.vacias=vacias

    # Indica si la sol. parcial es ya una solución factible (completa)
    def is_solution(self) -> bool:
        if primera_vacia(self.s)==None:
            return True
        return False

    # Si es sol. factible, la devuelve. Si no lanza excepción
    def get_solution(self) -> Sudoku:
        if self.is_solution():
            return self.s
        raise Exception()

    # Devuelve la lista de sus sol. parciales sucesoras
    def successors(self) -> Iterable["SudokuPS"]:
        if len(self.vacias)>0:
            mejor_posible=None
            for f, c in self.vacias:
                posibles =posibles_en(self.s ,f,c)
                if mejor_posible is None or len(posibles) <len(mejor_posible):
                    mejor_posible=posibles
                    f_mejor, c_mejor= f,c

            for num in mejor_posible:
                #s_copia = deepcopy(self.s)
                self.s[f_mejor][c_mejor]=num
                #vacias_copia = set(self.vacias)
                self.vacias.remove((f_mejor,c_mejor))

                yield SudokuPS(self.s,self.vacias)
                self.vacias.add((f_mejor,c_mejor))
            self.s[f_mejor][c_mejor]=0






# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # m_sudoku = [[0, 0, 0, 3, 1, 6, 0, 5, 9], [0, 0, 6, 0, 0, 0, 8, 0, 7], [0, 0, 0, 0, 0, 0, 2, 0, 0],
    #             [0, 5, 0, 0, 3, 0, 0, 9, 0], [7, 9, 0, 6, 0, 2, 0, 1, 8], [0, 1, 0, 0, 8, 0, 0, 4, 0],
    #             [0, 0, 8, 0, 0, 0, 0, 0, 0], [3, 0, 9, 0, 0, 0, 6, 0, 0], [5, 6, 0, 8, 4, 7, 0, 0, 0]]

    # El sudoku más difícil del mundo
    m_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    print("Original:")
    pretty_print(m_sudoku)
    print("\nSoluciones:")
    # Mostrar todas las soluciones
    # IMPLEMENTAR utilizando SudokuPS y BacktrackingSolver
    initial_ps=SudokuPS(m_sudoku,vacias(m_sudoku))
    for solution in BacktrackingSolver.solve(initial_ps):
         pretty_print(solution)
    print("<TERMINDADO>")  # Espera a ver este mensaje para saber que el programa ha terminado
