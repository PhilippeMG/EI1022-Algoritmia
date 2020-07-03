def solve(lista):

    pos= len(lista)//2

    if lista[pos-1]>lista[pos] and lista[pos+1]>lista[pos]:
        return pos

    elif lista[pos+1]<lista[pos]:
        izq = solve(lista[pos:])
        return pos+izq
    else:
        der = solve(lista[:pos+1])
        return der




l= [12,2,1,13]
print(l)
print(solve(l))