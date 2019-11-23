
from typing import *
from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution
import sys


def cryptoA_solver(word_list, word_solution, letters):

    class CryptoAPS(PartialSolution):
        def __init__(self, non_used_digits, dic_solution):
            #self.non_used_letters = non_used_lettersnew_ps
            self.non_used_digits = non_used_digits  # ¿..?
            self.dic_solution = dic_solution # Clave: letra, Valor: número
            self.n = len(dic_solution)

        def is_solution(self) -> bool:
 #           print("diccionario: ",self.dic_solution, "if ",self.n == len(letters), factible(self.dic_solution,letters,word_solution))
 #           print("letras: ",letters, "dic", self.n)
            #print(factible(self.dic_solution,letters,word_solution))
            return self.n == len(letters) and factible(self.dic_solution,letters,word_solution)  # True si -> longitud dic == letras que contiene el problema

        def get_solution(self) -> Solution:
            return numerate(self.dic_solution, word_list, word_solution)

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < len(letters):

                for num in self.non_used_digits: # Prueba cada número posible

                    child_dic_solution = self.dic_solution.copy() #Copia del diccionario
                    child_dic_solution[letters[self.n]] = num # Nuevo diccionario con el valor

                    child_non_used_digits = self.non_used_digits[:]
                    child_non_used_digits.remove(num)

                    if factible(child_dic_solution, word_list, word_solution):
                        yield CryptoAPS(child_non_used_digits,child_dic_solution)


    initial_ps = CryptoAPS( [1,2,3,4,5,6,7,8,9,0], {} )
    return BacktrackingSolver.solve(initial_ps)
def get_letters(word_list, word_solution):
    sol = [] # Se introducen las letras de derecha a izquierda
    todas=[]
    for w in word_list:
        todas.append(len(w))
    todas.append(len(word_solution))
  #  print(todas)
    bigest_word = max(todas)
  #  print(bigest_word)
  #  for i in range(1, len(bigest_word) + 1): # Índice letra
    for i in range(1, bigest_word + 1):
        for word in word_list: # Por cada word
           # print("get letters: palabra ",word)

            if i <= len(word) and word[-i] not in sol:  # Si el índice es válido y la letra no está en la lista
                sol.append(word[-i])


        if i <= len(word_solution) and word_solution[-i] not in sol:
            letter_sol = word_solution[-i]
            sol.append(letter_sol)

    return sol

def factible(dic, lista_palabras, solucion):
  #  print("en factible: ",lista_palabras," ", solucion)
    list_letters = get_letters(lista_palabras, solucion)
    if len(dic)!=list_letters:
        return True

    sol = []  # Se crea una lista con la suma de los elementos de todas las columnas
    mayor_palabra = max(lista_palabras)
    acarreo = 0
    for i in range(1, len(mayor_palabra) + 1):  # Índice letra
        suma = 0

        for palabra in lista_palabras:  # Por cada palabra

            if i <= len(palabra):  # Si el índice es válido para la palabra actual
                if palabra[-i] not in dic:  # Si la letra no está en el diccionario no se puede demostrar que no hay errores -> True
                    return True
                else:  # La letra está en diccionario
                    suma += dic[palabra[-i]]  # Suma columna

        suma += acarreo  # Se suma el acarreo que puede ser cero.
        acarreo = 0  # Una vez se suma el acarreo, éste pasa a valer 0
        if suma > 9:  # Si la suma es > 9 -> tiene acarreo
            acarreo = int(str(suma)[:-1])  # Magia
            suma = int(str(suma)[-1])  # Más magia

        if solucion[-i] not in dic:
            return True

        if suma != dic[solucion[-i]]:

            return False

        sol.append(suma)  # Se añade la suma de la columna a la lista

    if acarreo != 0:
        sol.append(acarreo)

    sol.reverse()
    #print(len(sol))
    #print(len(solucion))
    for i in range(len(sol)):
     #   print(sol[i])
      #  print(solucion[i])
       # print(dic)
        if not solucion[i] in dic:
            return True
        if sol[i] != dic[solucion[i]]:
            return False

    for palabra in lista_palabras:
        if dic[palabra[0]]==0:
            return False
    return True


def numerate(dic_solution, words_list, word_solution) -> str:
    solu = ''
    for word in words_list:
        for letter in word:
  #          print(dic_solution)
            solu += str(dic_solution[letter])
        solu += "+"
    solu = solu[:len(solu) - 1]
    solu += " = "
    for letter in word_solution:
       # print(letter)
       # print(dic_solution)
        solu += str(dic_solution[letter])

    return solu


if __name__ == '__main__':
    if 1 < len(sys.argv) == 2:
        # El parámetro es un fichero
        filename=sys.argv[-1]
        text_file = open(filename,encoding='utf-8')


        for line in text_file:
            datos = line.rstrip().split(" ")  # vector 4 elementos
            word_list = []  # Lista de palabras
            solucion = []
            for i in range(len(datos)-1):
                word_list.append(datos[i])
            solution=datos[-1]
    #        print("solucion: ",solution)
            list_letters = get_letters(word_list,solution)
            print("=================================================================================")
            print("lista: ",list_letters)

            print(word_list, solution)
            solucion=[]
            for sol in cryptoA_solver(word_list, solution, list_letters):
                solucion.append(sol)
            cadena=""
            for word in word_list:
                cadena+=word+"+"
            cadena=cadena[:len(cadena)-1]
            cadena= cadena + " = "+solution +" => "
            print(cadena,end="")

            if len(solucion)==1:
                print(solucion[0])
            else:
                print(len(solucion),"soluciones")
    elif len(sys.argv) >= 4: #Tiene que recibir por lo menos dos palabras y una solución (3 param) -> ( 1 + 3 = 4 )
        # Se recibe más de una parámetro. Los parámetros son el problema.
        word_list = [] # Lista de palabras
        solution = sys.argv[-1]
        for i in range(1, len(sys.argv) - 1):
            word_list.append(sys.argv[i])

        list_letters = get_letters(word_list,solution)
       # print("Word_list: {0}".format(word_list))
        #print("Solution: {0}".format(solution))
        #print("Letters of the problem: {0}".format(list_letters))

        solucion=[]
        for sol in cryptoA_solver(word_list, solution, list_letters):
            solucion.append(sol)
        cadena=""
        for word in word_list:
            cadena+=word+"+"
        cadena=cadena[:len(cadena)-1]
        cadena= cadena + " = "+solution +" => "
        print(cadena,end="")
        if len(solucion)==1:
            print(solucion[0])
        else:
            print(len(solucion),"soluciones")
            for r in solucion:
                print(r)



    else:
        print("ERROR: Incorrect parameters.")
        exit(-1)


