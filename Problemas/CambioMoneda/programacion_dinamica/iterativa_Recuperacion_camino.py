from typing import List, Tuple
from algoritmia.utils import infinity

def coin_change_iter(v: List[int], w: List[int], Q: int) -> Tuple[float, List[int]]:
    mem = {}
    mem[0, 0] = (0, ())
    for q in range(1, Q+1): mem[q,0] = (infinity, ())
    for n in range(1, len(v)+1):
        for q in range(1, Q+1):
            mem[q, n] = infinity, ()
            for i in range(q//v[n-1] + 1):
                q_previo, n_previo = q-i*v[n-1], n-1
                print(mem[q_previo, n_previo][0])
                mem[q, n] = min(mem[q,n], (mem[q_previo, n_previo][0] + i*w[n-1], (q_previo, n_previo, i)))
                print("-")
    weight = mem[Q, len(v)][0]
    sol = []
    q, n = Q, len(v)
    while (q,n) != (0,0):
        _, (qPrev, nPrev, i) = mem[q,n]
        sol.append(i) # usa el valor almacenado en mem
        q, n = qPrev, nPrev
    sol.reverse()
    return weight, sol

values, weights, quantity = [1, 2, 5], [1, 1, 4], 7
print(coin_change_iter(values, weights, quantity)) # output: (4, [1, 3, 0])
