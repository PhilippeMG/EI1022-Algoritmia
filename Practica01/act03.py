diccionario={"Borja": 21,"Diego":20,"Phil":24}

nombre=input("Dime un nombre: ")
if  nombre in diccionario:
    print(diccionario[nombre])
else:
    print("No sé su edad.")
