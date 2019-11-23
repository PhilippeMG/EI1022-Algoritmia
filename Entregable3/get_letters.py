def get_letters(word_list, word_solution):
    sol = [] # Se introducen las letras de derecha a izquierda
    todas=[]
    for w in word_list:
        todas.append(len(w))
   # todas.append(len(word_solution))
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

lista=["bala","lea"]
solucion="echan"
print(lista,solucion)
print(get_letters(lista,solucion))