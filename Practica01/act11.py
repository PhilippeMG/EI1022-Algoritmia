def cuadrados(lista):
    for elem in lista:
        yield elem**2

def first(n,iter):
    cont=0
    for elem in iter:
        yield elem
        cont+=1
        if c>=n:
            break



for c in first(4,cuadrados(range(100))):
    print(c)