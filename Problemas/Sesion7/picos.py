def busca_pico_rec(v):
    def rec(b, e):
        if e-b == 1:
            return b
        else:
            h = (b+e) // 2
            if v[h-1] <= v[h]:
                return rec(h, e)

            return rec(b, h)

            # v[h] es el mayor de sus hermanos
            return rec(h, h+1)

    return rec(0, len(v))

def busca_pico(v):
    inicio = 0
    fin = len(v)

    while(fin - inicio) > 1:
        medio = (fin + inicio) // 2
        if v[medio - 1] <= v[medio]:
            inicio = medio
        else:
            fin = medio
    return inicio

v = [10,20,15,2,23,90,67]
indiceA = busca_pico_rec(v)
indiceB = busca_pico(v)
print(indiceA, indiceB)