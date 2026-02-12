def massimoLista(lista): #Data una lista, calcola il massimo
    massimo=lista[0]
    for i in range (1,len(lista)):
        if lista[i]>massimo:
            massimo=lista[i]
    return(massimo)

def minimoLista(lista): #Data una lista, calcola il minimo
    minimo=lista[0]
    for i in range (1,len(lista)):
        if lista[i]<minimo:
            minimo=lista[i]
    return(minimo)