from typing import List, Tuple
from algoritmia.utils import infinity

def coin_change_iter_rs(v: List[int], w: List[int], Q: int) -> Tuple[float, List[int]]:
    current = [0] + [infinity]*Q
    previous = [None] * (Q + 1)
    for n in range(1, len(v) + 1):
        previous, current = current, previous
        for q in range(0, Q + 1):
            current[q] = min((previous[q-i*v[n-1]] + i*w[n-1] for i in range(q//v[n-1] + 1)),
                default = infinity)
            #current[q] = infinity
            #for i in range(q//v[n-1] + 1):
            # current[q] = min(current[q], (previous[q-i*v[n-1]] + i*w[n-1]))
    return current[Q]

values, weights, quantity = [1, 2, 5], [1, 1, 4], 7
print(coin_change_iter_rs(values, weights, quantity)) # output: 4
