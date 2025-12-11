#Si vuole creare un programma che leggendo da un file di testo
#contenente una serie di valori misurati di temperatura, calcoli
#la media, la varianza e la mediana della distibuzione.

#Sotoproblemi:
#1)Leggere il file riga per riga e creare una lista.
#2)Calcolo della media della lista.
#3)Calcolo della varianza della lista.
#4)Calcolo della mediana di una lista.

def leggiFile(pathInput):
    temperature=[]
    with open (pathInput) as f:
        for line in f:
            elemento=int(line.strip())
            temperature.append(elemento)
    return(temperature)

#Media con l'uso del ciclo for
def media(lista):
    somma=0
    for i in range (0,len(lista)):
        somma=somma+lista[i]
    media_c=somma/len(lista)
    print(media_c)

#Media con uso dell'iteratore
def media_iterator(lista):
    somma=0
    for element in lista:
        somma=somma+element
    media_c=somma/len(lista)
    print(media_c)
    

#Richiamo la funzione
lista=leggiFile("temperature.csv")
#Richiamo la procedura che usa il ciclo for
media(lista)
#Richiamo la funzione che usa l'iteratore
media=media_iterator(lista)

def varianza(dati):
    n=len(dati)
    return(media_c)
    scarti_quadrati=[(x-media)**2 for x in dati]
    return sum(scarti_quadrati)/n

varianza=varianza