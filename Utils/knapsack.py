from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed

def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self):         # IMPLEMENTAR: Añade los parámetros que tú consideres
            pass

        def is_solution(self) -> bool:      # IMPLEMENTAR
            pass

        def get_solution(self) -> Solution: # IMPLEMENTAR
            pass

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            pass

        def state(self) -> State:           # IMPLEMENTAR
            pass

        def f(self) -> Union[int, float]:   # IMPLEMENTAR
            pass

    initialPS = KnapsackPS()                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)

def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int,...], Tuple[int,...], int]:
    seed(42)
    weights = [int(random()*1000+1) for _ in range(num_objects)]
    values = [int(random()*1000+1) for _ in range(num_objects)]
    capacity = sum(weights)//2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7     # SOLUCIÓN: Weight=7,    Value=9
    # W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print (sol)
    print("\n<TERMINADO>")
