from typing import List

from algoritmia.utils import infinity

def coin_change_solve(v: List[int], w: List[int], Q: int) -> float:
    def L(q, n):
        if q == 0 and n == 0: return 0
        if q > 0 and n == 0: return infinity
        sol = infinity
        for i in range(q//v[n-1]+1):
            q_previo, n_previo = q-i*v[n-1], n-1
            sol = min(sol, L(q_previo, n_previo)+i*w[n-1])
        return sol
    return L(Q, len(v))

values, weights, quantity = [1, 2, 5], [1, 1, 4], 7
print(coin_change_solve(values, weights, quantity)) # output: 4
