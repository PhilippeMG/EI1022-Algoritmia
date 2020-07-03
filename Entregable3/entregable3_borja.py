
from typing import *
from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution
import sys


def cryptoA_solver(word_list, word_solution, letters):

    class CryptoAPS(PartialSolution):
        def __init__(self, non_used_digits, dic_solution):
            self.non_used_digits = non_used_digits
            self.dic_solution = dic_solution # Clave: letra, Valor: número
            self.n = len(dic_solution) # Por comodidad ;)

        def is_solution(self) -> bool:
            return self.n == len(letters) # True si -> longitud dic = letras que contiene el problema

        def get_solution(self) -> Solution:
            return numerate(self.dic_solution, word_list, word_solution)

        def successors(self) -> Iterable["PartialSolution"]:

            if self.n < len(letters):
                for num in self.non_used_digits: # Prueba cada número posible

                    child_dic_solution = self.dic_solution.copy() #Copia del diccionario
                    child_dic_solution[letters[self.n]] = num # Nuevo diccionario con el numero a probar

                    child_non_used_digits = self.non_used_digits[:] #Copia de la lista de dígitos no usados
                    child_non_used_digits.remove(num) # Borrado del numero a probar

                    if factible(child_dic_solution, word_list, word_solution):
                        yield CryptoAPS(child_non_used_digits, child_dic_solution)


    initial_ps = CryptoAPS( [0,1,2,3,4,5,6,7,8,9], {} )
    return BacktrackingSolver.solve(initial_ps)

def get_letters(word_list, word_solution):
    sol = [] # Se introducen las letras de derecha a izquierda

    tamanyo_palabras = []
    for w in word_list:
        tamanyo_palabras.append(len(w))
    tamanyo_palabras.append(len(word_solution))

    bigest_word = max(tamanyo_palabras)
    for i in range(1, bigest_word + 1):
        for word in word_list: # Por cada word
            if i <= len(word) and word[-i] not in sol:  # Si el índice es válido y la letra no está en la lista
                sol.append(word[-i])


        if i <= len(word_solution) and word_solution[-i] not in sol:
            letter_sol = word_solution[-i]
            sol.append(letter_sol)

    return sol


def factible(dic, lista_palabras, solucion):

    lista_longitud_palabras = []
    for w in lista_palabras:
        lista_longitud_palabras.append(len(w))

    lista_longitud_palabras.append(len(solucion))
    mayor_palabra = max(lista_longitud_palabras) # Longitud de la palabra con más caracteres
    acarreo = 0
    for i in range(1, mayor_palabra + 1):  # Índice letra
        suma_col = 0 # Suma de la columna

        # Si la letra de la solución no está en el diccionario -> True
        if solucion[-i] not in dic:  # No hay que comprobar si el índice es válido. Pues la suma de las palabras siempre es mayor.
            return True

        for palabra in lista_palabras:  # Por cada palabra
            if i <= len(palabra):  # Si el índice es válido para la palabra actual
                if palabra[-i] not in dic:  # Si la letra no está en el diccionario no se puede demostrar que no hay errores -> True
                    return True
                else:  # La letra está en diccionario
                    suma_col += dic[palabra[-i]]  # Suma columna

        suma_col += acarreo  # Se suma el acarreo que puede ser cero.
        acarreo = 0  # Una vez se suma el acarreo, éste pasa a valer 0
        if suma_col > 9:  # Si la suma es > 9 -> tiene acarreo
            acarreo = int(str(suma_col)[:-1])  # Magia
            suma_col = int(str(suma_col)[-1])  # Más magia

        if suma_col != dic[solucion[-i]]:
            return False

    if acarreo != 0 and acarreo != dic[solucion[0]]: # Si hay acarreo y no coincide con la primera letra de la solución -> False
        return False

    # Si hay cero en principio de palabra -> False
    for palabra in lista_palabras:
         if dic[palabra[0]] == 0:
             return False
    if dic[solucion[0]] == 0:
        return False

    return True


def numerate(dic_solution, words_list, word_solution) -> str:
    # Devuelve la solución numerada.
    solu = ''

    for word in words_list:
        for letter in word:
           solu += str(dic_solution[letter])
        solu += "+"
    solu = solu[:len(solu) - 1]
    solu += " = "

    for letter in word_solution:
        solu += str(dic_solution[letter])

    return solu

def formato(word_list,solution):
    # Da formato a la solución
    cadena = ""
    for word in word_list:
        cadena += word + "+"
    cadena = cadena[:len(cadena) - 1]
    cadena = cadena + " = " + solution + " => "
    return cadena

def filter_solutions(solutions):
    # Devuelve la solución al problema con el número de posibles soluciones si hay más de una.
    if len(soluciones) == 1:
        return solutions[0]
    else:
        return "{0} soluciones".format(len(solutions))

if __name__ == '__main__':
    if 1 < len(sys.argv) == 2:
        # El parámetro es un fichero
        filename = sys.argv[-1]
        text_file = open(filename, encoding='utf-8')

        for line in text_file:
            datos = line.rstrip().split(" ")  # vector 4 elementos
            word_list = []  # Lista de palabras
            for i in range(len(datos)-1):
                word_list.append(datos[i])

            word_solution = datos[-1]
            list_letters = get_letters(word_list, word_solution)

            soluciones = []
            for sol in cryptoA_solver(word_list, word_solution, list_letters):
                soluciones.append(sol)

            cadena = formato(word_list, word_solution)
            print(cadena, end="")
            print(filter_solutions(soluciones))


    elif len(sys.argv) >= 4: #Tiene que recibir por lo menos dos palabras y una solución (3 param) -> ( 1 + 3 = 4 )
        # Se recibe más de una parámetro. Los parámetros son el problema.
        word_list = [] # Lista de palabras
        word_solution = sys.argv[-1]
        for i in range(1, len(sys.argv) - 1):
            word_list.append(sys.argv[i])

        list_letters = get_letters(word_list, word_solution)

        soluciones = []
        for sol in cryptoA_solver(word_list, word_solution, list_letters):
            soluciones.append(sol)

        cadena = formato(word_list, word_solution)
        print(cadena, end="")
        print(filter_solutions(soluciones))
    else:
        print("ERROR: Incorrect parameters.")
        exit(-1)



