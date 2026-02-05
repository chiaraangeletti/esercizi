#Data una lista di elementi random interi nell'intervallo -10,+10
#calcolare il numero degli elementi pari e quelli dispari.
#1)Creare una lista di 10 elementi random
#2)Calcolare gli elementi pari e dispari

import random

def generaLista(lista):
    for i in range(0,10):
        elemento=random.randint(-10,10)
        lista.append(elemento)
        
def calcolaPariDispari(lista):
    pari=0
    dispari=0
    for elemento in lista: #iteratore
        if elemento%2==0:
            pari=pari+1
        else:
            dispari=dispari+1
    print(pari)
    print(dispari)
    
def generaListaMentre(lista):
    contatore=0
    while contatore<10:
        elemento=random.randint(-10,10)
        lista.append(elemento)
        contatore=contatore+1
    
if __name__=="__main__":
    myList=[]
    myList2=[]
    generaLista(myList)
    #Quando ad una procedura gli passo un arrey(vettore), viene passato per riferimento ovvero che non gli viene
    #passata la copia del valore ma l'indirizzo di memoria di quella variabile.
    calcolaPariDispari(myList)
    generaListaMentre(myList2)