#Scrivere un programma che generi una lista di numeri
#casuali compresi tra 0,100 che rappresentano misurazioni di intensità
#di un segnale. Il programma dopo aver generato la lista deve essere in
#grado di modificarla in questa maniera: gli elementi di indice pari
#devono esserre azzerati. Inoltre, dopo la modifica, si vuole contare il numero
#di elementi sopra una soglia numerica.

#Sottoproblemi:
#1) Generare una lista di  numeri compresi tra 1,1000
#2) Modificare la lista con la regola sopra
#3) Contare il numero di elementi sopra soglia

import random

def generaLista (n):
    mylist=[]   
    for i in range (0,n):
        elemento=random.randint(1,100)
        mylist.append(elemento)
    return(mylist)

#def proceduraGeneraLista (n,lista):   
#   for i in range (0,n):
#       elemento=random.randint(1,100)
#       mylist.append(elemento)
    
#listap=[]
#proceduraGeneraLista(6,listap)
#Oppure
#proceduraGeneraLista(lista=listap,n=6)

listax=generaLista(6)

def modificaLista(lista):
    n=len(lista)
    for i in range (0,n):
        if i%2==0:
            lista[i]=0
            
modificaLista(listax)

def soglia(lista,nsoglia):
    n=len(lista)
    contatore=0
    for i in range(0,n):
        if lista[i]>nsoglia:
            contatore=contatore+1
    return(contatore)

nsoglia=soglia(listax,50)

#def sogliaIteratore(lista,nsoglia):
#    contatore=0
#   for element in lista :
#       if element>nsoglia:
#           contatore=contatore+1
#   return(contatore)