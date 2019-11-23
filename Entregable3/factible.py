

def factible(lista_palabras, dic, solucion):
    # Devolverá True si -> Hay alguna letra que todavía no tiene valor y si la suma coincide con la solución
    # Devolverá False si -> Alguna suma no coincide con la solución

    sol = [] #Se crea una lista con la suma de los elementos de todas las columnas
    mayor_palabra = max(lista_palabras)
    acarreo = 0
    for i in range(1, len(mayor_palabra) + 1): # Índice letra
        suma = 0
        for palabra in lista_palabras: # Por cada palabra
            if i <= len(palabra):  # Si el índice es válido para la palabra actual
                if palabra[-i] not in dic:  # Si la letra no está en el diccionario no se puede demostrar que no hay errores -> True
                    return True
                else: # La letra está en diccionario
                    suma += dic[palabra[-i]] # Suma columna
        #print("Col: {0}: {1}".format(i,suma))
        # Comprobar si suma es correcta
        suma += acarreo #Se suma el acarreo que puede ser cero.
        acarreo = 0 # Una vez se suma el acarreo, éste pasa a valer 0
        if suma > 9: # Si la suma es > 9 -> tiene acarreo
            acarreo = int(str(suma)[:-1]) # Magia
            suma = int(str(suma)[-1]) # Más magia

        sol.append(suma) # Se añade la suma de la columna a la lista

    if acarreo != 0:
        sol.append(acarreo)

    sol.reverse()
    print(dic)
    print(sol)
    # Recorremos la lista sol y comprobamos que cada elemento coincida con la solución, si algun elem no coincide -> False

    #Se han recorrido todas las columnas y todos los elems coinciden
    return True

dic = {"p": 4, "a": 5, "l": 6}
lista_palabras = ["p", "pa", "pal"]
solucion = 382


print(factible(lista_palabras, dic, solucion))



