from typing import List, Tuple, Optional

def desglose2(valores: List[int], q: int) -> Optional[List[int]]:
    # creamos vector de índices para recorrer 'valores' de mayor a menor valor
    indices_ordenados = sorted(range(len(valores)), key=lambda i: -valores[i])
    #SALE EN EXAMEN
    res = [0]*len(valores)
    for i in indices_ordenados:
        res[i] = q//valores[i]
        q = q % valores[i]
        if q == 0:
            return res
    return None
print(desglose2([1,2,5,10], 6)) #[1, 0, 1, 0]
print(desglose2([2,5,10], 7))   #[1, 1, 0]
print(desglose2([1,9,15], 19))  #[4, 0, 1]
print(desglose2([2,9,15], 10))  #None


 # Coste temporal: O(|V| lg |V|)
 # ¿Es un algoritmo voraz válido? No para tod0 sistema monetario:
 #
 # V=(1,9,15) y Q=19: devuelve (4,0,1), que no es la solución óptima (1,2,0).
 #
 # V=(2,9,15) y Q=10: devuelve None, en lugar de (5,0,0).
 # Afortunadamente, la mayoría de sistemas monetarios (como el euro) utilizan valores de moneda que garantizan
 # que este algoritmo encontrará siempre el desglose óptimo.

