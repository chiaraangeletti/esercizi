#Funzioni

#lista1=[1,2,3,4]

#somma=0
#for element in lista1:
    #somma=somma+element
#print(somma)

#lista2=[2,3,4,5]

#somma=0
#for element in lista2:
    #somma=somma+element
#print(somma)

#stiamo chiedendo la stessa cosa ma con una lista diversa e in informatica non si fa
#perché si utilizzano le funzioni ovvero un pezzo di codice generico che
#funziona sulla base di input che vengono passati dall'esterno.

#def sommaLista (lista):
    #somma=0
    #for element in lista:
        #somma=somma+element
    #print(somma)
    
#lista=[1,2,3,4]
#sommaLista(lista)
#lista2=[2,3,4,5]
#sommaLista(lista2)

#Scrivere una funzione che data una lista stampi a video il numero degli elementi pari.
#le variabili all'interno della funzione, come ad esempio la variabile somma, esistono
#solo all'interno della fenzione e non all'esterno.

def numeriPari (lista):
    nPari=0
    for element in lista:
        if element%2==0:
            nPari=nPari+1
    print(nPari)
        
lista3=[1,2,3,4,5,6]
numeriPari(lista3)
lista4=[2,4,6,10,3,1]
numeriPari(lista4)

            