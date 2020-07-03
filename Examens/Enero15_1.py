def buscar_indice_solitario(v):
    def rec(inicio,final):
        if final - inicio == 1:
            return inicio
        medio = (inicio+final)//2

        if medio%2==0:
            return rec(medio,final)
        return rec(inicio,medio)
    return rec(0,len(v))

v = [2,3,3,4,4,6,6,7,7]
print(v)
pos = buscar_indice_solitario(v)
print("indice: ",pos, "elemento: ", v[pos])
