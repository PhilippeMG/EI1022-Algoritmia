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



def filter(cond,iter):
    for elem in iter:
        if(cond(elem)):
            yield elem

def take_while(cond,iter):
    for elem in iter:
        if cond(elem):
            yield elem
        else:
            break






for c in take_while(lambda n: n<100, range(50, 200)):
    print(c)
print("----------------")
for c in take_while(lambda n: n%2 == 0, [2,4,5,7,2]):
    print(c)

#for c in filter(lambda  n: n%2==0,first(4,cuadrados(range(1000)))):
 #   print (c)