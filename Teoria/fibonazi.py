def fib(n: int)-> int:
    global steps
    steps +=1
    if n ==0: return 0
    if n ==1: return 1
    return fib(n-2)+ fib(n-1)

steps = 0
print(fib(20), steps)