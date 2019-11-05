from Utils.bt_scheme import  BacktrackingSolver, PartialSolution, Solution
from typing import *



class NQuennsPS(PartialSolution):
    def __init__(self, N: int, sol: Tuple[int,...]):
        self.N = N
        self.sol = sol

    def is_solution(self) -> bool:
        return len(self.sol) == self.N

    def get_solution(self) -> Solution:
        return self.sol

    def _is_valid(self, r):
        if r in self.sol: return False
        nd = len(self.sol)
        for j in range(nd):
            if nd - j == abs(r - self.sol[j]):
                return False
        return True

    def successor(self) -> List["PartialSolution"]:
        res = []
        if len(self.sol) < self.N:
            for r in range(self.N):
                if self.is_valid(r):
                    res.append(NQuennsPS(self.N, self.sol + (r,)))

        return res


# if __name__ == '__main__':
#     N = 14
#     initial_ps = NQuennsPS(N, ())
#     c = 0
#     for sol in BacktrackingSolver.solve(initial_ps):
#         print(sol)
#         c += 1
#     print(c)

if __name__ == "__main__":
    N = 4
    initial_ps = NQuennsPS(N, ())
    for sol in BacktrackingSolver.solve(initial_ps):
        print(sol)