from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed

def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self,solution,current_weight, current_value):         # IMPLEMENTAR: Añade los parámetros que tú consideres
            #self.weights = weights
            #self.values = values
            #self.capacity = capacity
            self.solution = solution
            self.current_weight = current_weight
            self.current_value=current_value
            self.n=len(solution)
        def is_solution(self) -> bool:      # IMPLEMENTAR
            return self.n == len(weights)

        def get_solution(self) -> Solution: # IMPLEMENTAR
            #print(self.current_weight,"",self.current_value)
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            if self.n<len(weights):
                if self.current_weight+weights[self.n]<=capacity:
                    yield KnapsackPS(self.solution+(1,),self.current_weight+weights[self.n],self.current_value + values[self.n])

                yield KnapsackPS(self.solution+(0, ), self.current_weight, self.current_value)

            pass

        def state(self) -> State:           # IMPLEMENTAR
            return self.n ,self.current_weight

        def f(self) -> Union[int, float]:   # IMPLEMENTAR
            return -self.current_value

    initialPS = KnapsackPS((),0,0)                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)

def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int,...], Tuple[int,...], int]:
    seed(42)
    weights = [int(random()*1000+1) for _ in range(num_objects)]
    values = [int(random()*1000+1) for _ in range(num_objects)]
    capacity = sum(weights)//2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    W, V, C = [1, 4, 3, 2], [2, 3, 2, 4], 7
    #W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7     # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print (sol)
    print("\n<TERMINADO>")
