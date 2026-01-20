#Scrivere un programma che dati due numeri
#interi random in un intervallo 0,100 ne calcoli
#la somma, la differenza e controlli se la differenza è
#minore di una certa soglia fissata a priori nel main.
#Sottoprobelmi:
#1) Somma di due numeri (procedura percè non mi serve più per il continuo del programma)
#2)Differenza tra due numeri (funzione perchè mi serve per il continuo del programma)
#3)Verificare se un numero è minore di una soglia (procedura perchè non mi serve più per il continuo del programma)

import random

def sommaNumeri (a,b):
    somma=a+b
    print(somma)
    
def differenzaNumeri (a,b):
    diff=a-b
    return(diff)

def minoreSoglia (differenza,soglia):
    if differenza < soglia:
        print("La differenza dei due numeri e' minore della soglia")

if __name__ == '__main__':
    numeroUno=random.randint(0,100)
    numeroDue=random.randint(0,100)
    numeroSoglia=50
    sommaNumeri(numeroUno,numeroDue)
    diff=minoreSoglia(numeroUno,numeroDue)
    minoreSoglia(diff,numeroSoglia)