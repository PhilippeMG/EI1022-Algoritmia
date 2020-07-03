

class Ascension:
    def __init__(self,altitud,pico,pais):
        self.altitud= altitud
        self.pico=pico
        self.pais=pais
        self.repeticiones = 1

def crear_lista_ascensiones(nombre_fichero):
    fichero = open(nombre_fichero)
    lista_ascensiones=[]
    for linea in (fichero):
        datos = linea.strip().split("-")
        ascension = Ascension(datos[0],datos[1],datos[2])
        añadido= False
        for montañas in lista_ascensiones:
            if montañas.pico==ascension.pico:
                montañas.repeticiones+=1
                añadido=True
                break
        if añadido == False:
            lista_ascensiones.append(ascension)
    fichero.close()
    return lista_ascensiones



lista =crear_lista_ascensiones("fichero.txt")
for montaña in lista:
    print(montaña.altitud,montaña.pico,montaña.pais,montaña.repeticiones)