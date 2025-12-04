#Scrivere un programma che calcoli il minimo e il massimo di una lista
#di interi random compresi nell'intervallo 0,100.

#Sottoproblemi:
#1)Calcolare il minimo di una lista
#2)Calcolare il massimo di una lista
#3)Generare una lista di n numeri interi random nell'intervallo 0,100

import random

def generaLista(n):
    mylist=[]
    for i in range (0,n):
        element=random.randint(0,100)
        mylist.append(element)
    return(mylist)

def minimoLista(lista,n):
    minimo=lista[0]
    for i in range (1,n):
        if lista[i]<minimo:
            minimo=lista[i]
    print(minimo)
    
def massimoLista(lista,n):
    massimo=lista[0]
    for i in range (1,n):
        if lista[i]>massimo:
            massimo=lista[i]
    print(massimo)

if __name__=="__main__": #se il programma parte, fai le cose seguenti:
    dimensione=10
    listaInt=generaLista(dimensione)
    minimoLista(listaInt,dimensione)
    massimoLista(listaInt,dimensione)
    
#Ogni programma finisce all'interno di un processo, una struttura particolare che viene gestita dal processore (CU).
#Ogni processo che va allocato all'interno della RAM ha due aree di memoria separate che sono lo stack e l'heap.
#Lo stack è una area di tipo lifo(pila) ovvero una struttura informatica dove all'interno viene inserito un record,
#uno sopra l'altro. Lifo (last in first out) la cima della pila è il primo che viene estratto da essa.
#L'heap è un'altra area di memoria simile alla RAM, quindi fatta da celle dentro le quali risiedono i dati. Ha la
#stessa struttura volatile della RAM. Nello stack ci vanno tutte le chiamate statiche mentre nell'heap ci vanno le
#chiamate dinamiche. Nel primo ci vanno gli indirizzi di memoria(riferimenti), e nel secondo ci vanno gli oggetti.
#Nello stack vengono allocate le variabili locali, che non sono oggetti.