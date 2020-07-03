def mostrar_variedad_mnayor_cosecha_anual(matriz,nombres):
    maximo=0
    posicion=0

    for col in range(len(matriz[0])):
        for fil in range(len(matriz)):
            if matriz[fil][col]>=maximo:
                maximo=matriz[fil][col]
                posicion=fil
        maximo=0
        print("Fruta con mayor cosecha el año",col,":",nombres[posicion])

#---------------------------------------------------------------------------
def producción_media(matriz,índice_cíctrico):
    suma=0
    for col in range(len(matriz[0])):
        suma+=matriz[índice_cíctrico][col]
    return suma/len(matriz[0])
#---------------------------------------------------------------------------
def periodo_más_largo(matriz,nombres,cítrico):
    fila=0
    for nombre in nombres:
        if nombre==cítrico:
            break
        fila+=1
    media = producción_media(matriz,fila)
    maximo=0
    actual=0
    for col in range(len(matriz[0])):
        if matriz[fila][col]>media:
            actual+=1
        else:
            if actual>maximo:
                maximo=actual
            actual=0

    if actual > maximo:
        return actual
    return maximo

#---------------------------------------------------------------------------

variedades = ['Clemevilla','Navel Lane Late', 'Navelina','Hernandina']
produccion = [
    [150,110,140,130,120],
    [50,80,60,70,75],
    [119,100,145,120,120],
    [160,90,150,120,130]
]
mostrar_variedad_mnayor_cosecha_anual(produccion,variedades)
print(producción_media(produccion,0))
print(periodo_más_largo(produccion,variedades,"Clemevilla"))

