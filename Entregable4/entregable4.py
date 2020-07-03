from Utils.skylineviewer import SkylineViewer
from typing import *
import sys
from time import time



def leer_fichero(fichero):
    file = open(fichero, encoding='utf-8')
    buildings = []
    for line in file:
        x1, y, x2 = line.split()  #Sepraramos los elementos del vector en 3 atributos
        buildings.append((int(x1),int(y),int(x2)))  #Los metemos en la lista como enteros
    return buildings

def skyline(buildings: List[Tuple[int, ...]], inicio: int, final: int) -> List[int]:

    def get_solucion(skyline_left: List[int], skyline_right: List[int]) -> List[int]:

        skyline_left.append(0)  # Insertamos un 0 para delimitar la altura del ultimo edificio
        skyline_right.append(0)
        left = right = height_left = height_right = previous = 0  #Inicializamos  a 0
        solucion = []

        while left < len(skyline_left) - 1 and right < len(skyline_right) - 1:
            if skyline_left[left] < skyline_right[right]:
                height_left = skyline_left[left + 1]
                x = skyline_left[left]
                left += 2
            elif skyline_right[right] < skyline_left[left]:
                height_right = skyline_right[right + 1]
                x = skyline_right[right]
                right += 2
            else:
                height_right = skyline_right[right + 1]
                height_left = skyline_left[left + 1]
                x = skyline_right[right]
                right += 2
                left += 2
            max_height = max(height_left, height_right)
            if previous is not max_height:
                solucion.append(x)
                solucion.append(max_height)
                previous = max_height
        for i in range(left, len(skyline_left)):
            solucion.append(skyline_left[i])
        for i in range(right, len(skyline_right)):
            solucion.append(skyline_right[i])
        solucion.pop()  #Quitamos el ultimo elemento que es el 0 que añadimos al principio
        return solucion
    #Codigo adaptado de problemas session 7

    if final - inicio == 1:
        return [buildings[inicio][0], buildings[inicio][1], buildings[inicio][0] + buildings[inicio][2]]
    if final - inicio == 2:
        return get_solucion([buildings[inicio][0], buildings[inicio][1], buildings[inicio][0] + buildings[inicio][2]], [buildings[inicio + 1][0], buildings[inicio + 1][1], buildings[inicio + 1][0] + buildings[inicio + 1][2]])
    else:
        mitad = (inicio + final) // 2
        return get_solucion(skyline(buildings, inicio, mitad), skyline(buildings, mitad, final))



if __name__== '__main__':
    if len(sys.argv) >= 2:
        #start_time = time() #Obtenemos el tiempo de inicio

        # El parámetro es un fichero
        filename = sys.argv[-1]
        buildings = leer_fichero(sys.argv[1])
        perfil = skyline(buildings, 0, len(buildings))
        for p in perfil:
            print(p, end=" ")
        print("")
        #elapsed_time = time() - start_time #Calculamos el tiempo de ejecucion
        #print("\nElapsed time: %.10f seconds." % elapsed_time)
        if len(sys.argv) == 3 and sys.argv[2] == "-g":
        # Extensión del entregable
            viewer = SkylineViewer(perfil)
            for edificio in buildings:
                viewer.add_building(edificio)
            viewer.run()
    else:
        print("Incorrect number of parameters.")