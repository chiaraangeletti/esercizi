#Data una serie di 10 misurazioni randomiche intere, comprese tra
#due intervalli forniti da tastiera, produrre in output un file di testo che
#abbia i valori, la media dei valori, il numero di valori sopra una certa soglia
#fissata a massimo delle misurazioni meno 10.
#1) Creare una lista di 10 misurazioni random (procedura)
#2) fare la media dei valori della lista (funzione)
#3) Calcolare la soglia (funzione)
#4) Contare il numero di valori sopra la soglia (procedura)

import random
from kallax import * #Dal file kallax importa tutto ciò che c'è dentro

def creaLista(lista):
    nUno=input("Inserire il primo estremo")
    nUno=int(nUno)
    nDue=input("Inserire il secondo estremo")
    nDue=int(nDue)
    for i in range (0,10):
        if nDue>nUno:
            elemento=random.randint(nUno,nDue)
        else:
            elemento=random.randint(nDue,nUno)
        lista.append(elemento)
        
def media(lista):
    sommaElementi=0
    numeroElementi=0
    for elemento in lista:
        sommaElementi=sommaElementi+elemento
    mediaElementi=sommaElementi/len(lista)
    return(mediaElementi)

def calcolaSoglia(lista):
    massimo=massimoLista(lista)
    soglia=massimo-10
    return(soglia)

def sopraSoglia(lista,soglia):
    contatore=0
    for i in range (0,len(lista)):
        if lista[i]>soglia:
            contatore=contatore+1
    print(contatore)

if __name__=="__main__":
    listaM=[]
    creaLista(listaM)
    mediaValori=media(listaM)
    sogliaValori=calcolaSoglia(listaM)
    sopraSoglia(listaM,sogliaValori) 
    minimo=minimoLista(listaM) #Funzione importata da kallax
    print(minimo)