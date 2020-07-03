from algoritmia.schemes.decreaseandconquer import IDecreaseAndConquerProblem, DecreaseAndConquerSolver
class BuscaEnCreciente(IDecreaseAndConquerProblem):
    def __init__(self, v, b, e):
        self.v = v
        self.b = b
        self.e = e

    def is_simple(self) -> "bool":
        return self.e - self.b == 1

    def trivial_solution(self) -> "Solution":
        if self.v[self.b] == self.b: # Si el elemento del vector es igual al índice
            return self.b if self.v[self.b] == self.b else None


    def decrease(self) -> "IDecreaseAndConquerProblem":
        punto_medio = (self.e + self.b) // 2
        if self.v[punto_medio] > punto_medio:
            return BuscaEnCreciente(self.v, self.b, punto_medio)
        if self.v[punto_medio] < punto_medio:
            return BuscaEnCreciente(self.v, punto_medio, self.e)

        # El elemento es igual al índice
        return BuscaEnCreciente(self.v, punto_medio, punto_medio+1) #Encontrado

if __name__ == "__main__":
    v = [-10,-5,1,3,6]
    problem = BuscaEnCreciente(v,0,len(v))
    print(DecreaseAndConquerSolver().solve(problem))


