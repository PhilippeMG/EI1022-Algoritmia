def solve2(enteros : [int], e : int)-> int:
    global steps


    if len(enteros)<=0 or enteros[0] > e or enteros[len(enteros)-1] < e : return 0
    steps += 1
    print("Lista: ",enteros)

    if len(enteros)==1:
        if e in enteros:
            return 1
        else:
            return 0

    izq=enteros[:len(enteros)//2]
    der= enteros[len(enteros)//2:]
    return solve2(izq,e)+solve2(der,e);

def solve(enteros : [int], e : int)-> int:
    if e not in enteros:
        return 0
    pos = len(enteros)//2

    izq =buscar_ini(enteros,e,pos)
    print("izq: ",izq)
    der = buscar_fin(enteros,e,pos)
    print("der: ",der)

    print("izq: ",izq, " der: ",der)

    return der -izq +1

def buscar_ini(enteros : [int], e : int,pos:int)-> int:

    if enteros[pos] < e:
        if pos+pos//2<len(enteros):
            return buscar_ini(enteros,e,pos+pos//2)
        else:
            return buscar_ini(enteros,e,len(enteros)-1)

    if enteros[pos]>e:
        return buscar_ini(enteros,e,pos//2)
    if enteros[pos] == e and pos -1 < 0 or enteros[pos-1] != e:
        return pos
    elif enteros[pos] == e and enteros[pos-1]==e:
        return buscar_ini(enteros,e,pos-1)


def buscar_fin(enteros : [int], e : int,pos:int)-> int:

    if enteros[pos] < e:
        if pos+pos//2<len(enteros):
            return buscar_fin(enteros,e,pos+pos//2)
        else:
            return buscar_fin(enteros,e,len(enteros)-1)

    if enteros[pos]>e:
        return buscar_fin(enteros,e,pos//2)
    if enteros[pos] == e and pos + 1 >= len(enteros) or enteros[pos + 1] != e:
        return pos
    elif enteros[pos] == e and enteros[pos+1]==e:
        return buscar_fin(enteros,e,pos+1)


    return -1
steps = 0
lista = [-2,-2,0,1,2,2,3,4,4,4,5,5,5]
entero =4
print(lista)
print(solve(lista,entero))
#print("Repeticiones: ",steps)
