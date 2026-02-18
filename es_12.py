from kallax import*

def selectionSort(lista):
    for i in range (0,len(lista)):
        minimo=minimoLista(lista[i:])
        indiceMin=lista.index(minimo)
        lista[indiceMin]=lista[0]
        lista[0]=minimo
    print(lista)