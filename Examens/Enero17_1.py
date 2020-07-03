def menor_numero_intervalos(puntos: [float], a: float) -> int:
    puntos.sort()
    # coste O(N log N)
    num=puntos[0]
    cont=1
    for dato in puntos:
        if dato>num+a:
            num=dato
            cont+=1
    return cont

lista = [1.0, 3.5,9,2.5,7]
intervalo = 3
print(menor_numero_intervalos(lista, intervalo))