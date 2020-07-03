from typing import List, Tuple
from algoritmia.utils import infinity

def coin_change_mem_solve_final(v: List[int], w: List[int], Q: int) -> Tuple[float, List[int]]:
    def L(q, n):
        if q == 0 and n == 0: return 0
        if q > 0 and n == 0: return infinity
        if (q, n) not in mem:
            mem[q, n] = infinity, ()
            for i in range(q//v[n-1]+1):
                q_previo, n_previo = q-i*v[n-1], n-1
                mem[q, n] = min(mem[q,n], (L(q_previo, n_previo) + i*w[n-1], (q_previo, n_previo)))
        return mem[q, n][0]

    mem = {}
    weight = L(Q, len(v))
    q, n = Q, len(v)
    sol = []
    while (q, n) != (0,0):
        _, (qPrev, nPrev) = mem[q,n]
        sol.append((q-qPrev)//v[n-1]) # averigua monedas utilizadas
        q, n = qPrev, nPrev
    sol.reverse()
    return weight, sol
values, weights, quantity = [1, 2, 5], [1, 1, 4], 7
print(coin_change_mem_solve_final(values, weights, quantity)) # output: (4, [1, 3, 0])
