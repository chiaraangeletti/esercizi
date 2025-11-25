#Scrivere una procedura che data una lista e un numero chiamato alfa
#stampi a video il numero degli elementi della lista più grandi di alfa.

def contaMaggioreAlfa (lista,alfa):
    numeriMaggiori=0
    for element in lista:
        if alfa<element:
            numeriMaggiori=numeriMaggiori+1
    print(numeriMaggiori)
    
alfa=4
lista=[1,3,4,5,6,7]
contaMaggioreAlfa(lista,alfa)