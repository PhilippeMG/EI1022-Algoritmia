lista=[]
while True:
    num = int(input("Introduce un numero: "))
    if(num<0): break
    lista.append(num)


lista.sort()

for elem in lista:
    print(elem)
