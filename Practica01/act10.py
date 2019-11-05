def cuadrados(lista):
    for elem in lista:
        yield elem**2


for c in cuadrados([1,2,10,4,5]):
    print(c)