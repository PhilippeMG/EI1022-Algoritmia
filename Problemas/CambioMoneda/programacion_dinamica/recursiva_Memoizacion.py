from typing import List
from algoritmia.utils import infinity

def coin_change_mem_solve(v: List[int], w: List[int], Q: int) -> float:
    def L(q, n):
        if q == 0 and n == 0: return 0
        if q > 0 and n == 0: return infinity
        if (q,n) not in mem:
            mem[q,n] = infinity
            for i in range(q//v[n-1] + 1):
                q_previo, n_previo = q-i*v[n-1], n-1
                mem[q,n] = min(mem[q,n], L(q_previo, n_previo) + i*w[n-1])
        return mem[q,n]
    mem = {}
    return L(Q, len(v))

values, weights, quantity = [1, 2, 5], [1, 1, 4], 7
print(coin_change_mem_solve(values, weights, quantity)) # output: 4
