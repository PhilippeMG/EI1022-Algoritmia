def numerate(dic_solution, words_list, word_solution) -> str:
    solu = ''
    for word in words_list:
        for letter in word:
           solu += str(dic_solution[letter])
        solu += "+"
    solu=solu[:len(solu)-2]
    solu += "="

    for letter in word_solution:
        solu += str(dic_solution[letter])

    return solu
dic= {"s":9,"e":5,"n":6,"d":7,"m":1,"o":0,"r":8,"y":2}
print(dic)
words_list=["send", "more"]
word_solution="money"
print(numerate(dic,words_list,word_solution))