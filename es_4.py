import random

somma=0
mazzo=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
contatore=0
bj={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":10,"Q":10,"K":10}

while somma<=21:
    indice=random.randint(1,13)
    carta_estratta=mazzo[indice]
    valore=bj[carta_estratta]
    somma=somma+valore
    contatore=contatore+1