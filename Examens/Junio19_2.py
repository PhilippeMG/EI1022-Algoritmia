def nuevo_elemento(lAnt,lNuevo):
    pos=len(lNuevo)//2
    if pos==0 or pos == len(lAnt)or lNuevo[pos]>lAnt[pos-1] and lNuevo[pos]!=lAnt[pos]:
        return lNuevo[pos]
    elif lNuevo[pos] == lAnt[pos]:
        return nuevo_elemento(lAnt[pos:],lNuevo[pos:])
    else:
        return nuevo_elemento(lAnt[:pos], lNuevo[:pos])

ant=[1,4,5,7]
nuevo=[1,2,4,5,7]
print("\n", ant, "\n", nuevo)

print(nuevo_elemento(ant,nuevo))

#Costes Temporal   O(lgN)     Espacial O(lgN)² ?