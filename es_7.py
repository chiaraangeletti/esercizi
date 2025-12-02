#Dati quattro numeri interi generati randomicamente, creare una tupla che contenga
#Il maggiore dei primi due e il minore degli ultimi due.

#Sottoproblemi: trovare il maggiore di due numeri
#               trovare il minore di due numeri

import random

def maggiore(a,b):
    if a>b:
        return a
    else:
        return b

def minore(c,d):
    if c<d:
        return c
    else:
        return d
    
nUno=random.randint
nDue=random.randint
nTre=random.randint
nQuattro=random.randint

risultato1=maggiore(nUno,nDue)
risultato2=minore(nTre,nQuattro)

risultato=(risultato1,risultato2)