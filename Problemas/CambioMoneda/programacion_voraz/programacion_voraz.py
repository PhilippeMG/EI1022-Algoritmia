from typing import List, Tuple, Optional


def desglose1(valores: List[int], q: int) -> Optional[List[int]]:
    res = []
    for v in valores:
        res.append(q//v)
        q = q % v
        if q == 0:
            return res + [0]*(len(valores)-len(res))
    return None
print(desglose1([1,2,5,10], 6)) # [6, 0, 0, 0]
print(desglose1([2,5,10], 7))   # None
print(desglose1([1,9,15], 19))  # [19, 0, 0]


#  Coste temporal: O(|V|)
#  ¿Es un algoritmo voraz válido? No:
#     Para V=(1,2,5,10) y Q=6 devuelve 6 monedas de
#     valor 1, que no es la solución óptima.
# Para V=(2,5,10) y Q=7 no devuelve ninguna solución.
