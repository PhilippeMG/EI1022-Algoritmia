from math import ceil

from Utils.bab_scheme import BabPartialSolution, BabSolver, Solution
from random import seed, randint
from itertools import groupby
from typing import *


def binpacking_solve(objects: List[int], capacity: int):
    class BinPackingBabPS(BabPartialSolution):
        def __init__(self, decisions: Tuple[int, ...], container_weights: Tuple[int, ...]):
            self.decisions = decisions
            self.container_weights = container_weights
            self.n = len(decisions)
            self._opt = self.calc_opt_bound()
            self._pes = self.calc_pes_bound()

        # TODO: IMPLEMENTAR - Relaja el problema. Trata los objetos que quedan como si fueran un líquido
        def calc_opt_bound(self) -> Union[int, float]:
            if len(self.container_weights) > 0:
                mayor_hueco = capacity - min(self.container_weights)
            else:
                mayor_hueco = capacity

            suma_caben = suma_no_caben = 0
            for num_objeto in range(self.n, len(objects)):
                if objects[num_objeto] <= mayor_hueco:
                    suma_caben += objects[num_objeto]
                else:
                    suma_no_caben += objects[num_objeto]

            if self.n < len(objects):
                smallest_object = min(objects[self.n:]) # "self.n:" operador de corte. Obtiene desde self.n hasta el final
            else:
                smallest_object = 0

            for container_weight in self.container_weights:
                hueco_contenedor = capacity - container_weight
                if hueco_contenedor >= smallest_object:
                    suma_caben -= hueco_contenedor
                    if suma_caben <= 0:
                        suma_caben = 0
                        break
            suma_resto = suma_caben + suma_no_caben

            return  len(self.container_weights) + ceil(suma_resto / capacity) # ceil redondea hacia arriba


        # TODO: IMPLEMENTAR - Algoritmo voraz. Completa la solución parcial actual con "En el primero en el que quepa"
        def calc_pes_bound(self) -> Union[int, float]:
            cws = list(self.container_weights)

            # for num_objeto in range(self.n, len(objects)):
            #     ha_cabido = False
            #     for num_contenedor in range(len(cws)):
            #         if objects[num_objeto] + cws[num_contenedor] <= capacity:
            #             cws[num_contenedor] += objects[num_objeto]
            #             ha_cabido = True
            #             break
            #     if ha_cabido == False:
            #         cws.append(objects[num_objeto])

            for num_objeto in range(self.n, len(objects)):
                for num_contenedor in range(len(cws)):
                    if objects[num_objeto] + cws[num_contenedor] <= capacity:
                        cws[num_contenedor] += objects[num_objeto]
                        break
                else:
                    cws.append(objects[num_objeto])

            return len(cws)

        def is_solution(self) -> bool:
            return self.n == len(objects)

        def get_solution(self) -> Solution:
            return self.decisions

        def successors(self) -> Iterable["BinPackingBabPS"]:
            if self.n < len(objects):
                object_weight = objects[self.n]
                for num_container, container_weight in enumerate(self.container_weights):
                    if container_weight + object_weight <= capacity:
                        list_cw = list(self.container_weights)  # copia tupla a lista
                        list_cw[num_container] += object_weight
                        yield BinPackingBabPS(self.decisions + (num_container,), tuple(list_cw))
                num_container = len(self.container_weights)
                yield BinPackingBabPS(self.decisions + (num_container,), self.container_weights + (object_weight,))

    initial_ps = BinPackingBabPS((), ())
    return BabSolver.solve_minimization(initial_ps)


def show_solution_grouped_by_containers(sol):
    print("\nSOLUTION GROUPED BY CONTAINERS (shows the weights of objects in each container):")
    for pos, g in groupby(sorted([o, i] for i, o in enumerate(sol)), lambda e: e[0]):
        print("\t{}: {}".format(pos, [objs[e[1]] for e in g]))


def create_exact_binpacking_problem(num_containers, objects_per_container):
    seed(5)
    objects = []
    num_c = num_containers
    num_e_c = objects_per_container
    min_v = 25
    max_v = 35
    capacity = max_v * num_e_c + 0
    for ic in range(num_c):
        s = 0
        for ie in range(num_e_c - 1):
            o = randint(min_v, max_v)
            objects.append(o)
            s += o
        objects.append(capacity - s)
    return capacity, sorted(objects, reverse=True)


# PROGRAMA PRINCIPAL -------------------------------------------------------
if __name__ == "__main__":
    # Descomenta la instancia del problema que quieras resolver:
    C, objs = 10, [6, 6, 3, 3, 2, 2, 2, 2, 2, 2]  # SOLUCIÓN ÓPTIMA: 3 contenedores
    # C, objs = create_exact_binpacking_problem(6, 3)  # SOLUCIÓN ÓPTIMA: 6 contenedores
    # C, objs = create_exact_binpacking_problem(12, 3) # SOLUCIÓN ÓPTIMA: 12 contenedores

    print("PROBLEM TO SOLVE:")
    print("\tContainer capacity:", C)
    print("\tObjects (weights):", objs)

    solution = binpacking_solve(objs, C)

    print("\nBEST SOLUTION:")
    print("\tB&B solution: {0} containers. Details: {1}".format(max(solution) + 1, solution))

    show_solution_grouped_by_containers(solution)