def fib_mem(n: int) -> int:
    def _f(n: int) -> int:
        global steps
        if n == 0: return 0
        if n == 1: return 1
        steps += 1

        if n not in mem:
            mem[n] = _f(n-2) + _f(n-1)
        return mem[n]
    mem = {}
    return _f(n)

steps = 0
print(fib_mem(20), steps)