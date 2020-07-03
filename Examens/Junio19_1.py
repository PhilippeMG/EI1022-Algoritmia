def cortar_cuerda(M, L,B, P):
    indices_ordenados=sorted(range (len(L)), key = lambda i : -B[i]/L[i])
    res= [0] *len(L)
    for i in indices_ordenados:
        res[i]=min(P[i],M//L[i])
        M-=res[i]*L[i]
    return res


M=100
L=[50,10,30,40]
B=[2,4,5,6]
P=[2,3,1,0]
sol= cortar_cuerda(M,L,B,P)
print(sol)
#coste Espacial, O(N)
#coste Temporal, O(N*LgN)