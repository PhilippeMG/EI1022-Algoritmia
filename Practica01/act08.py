class Estudiante:
    notas = {}

    def __init__(self,name):
        self.name=name
    def califica(self,asinatura,nota):
        self.notas[asinatura]=nota
    def nota(self,asignatura):
        return self.notas[asignatura]
    def media(self):
       n=len(self.notas)
       return sum(self.notas.values())/n if n!=0 else None


    def muestra_expediente(self):
        print("Nombre:" +self.name)

        for asig in self.notas:
            print ("Asignatura: "+asig+" Nota: "+self.notas[asig])

      #  for asig, nota in self.notas.items():
      #      print ("Asignatura: "+asig+" Nota: "+nota)


