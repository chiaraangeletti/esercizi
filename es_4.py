#1) Estrarre 3 carte da un mazzo(lista)
# [1,2,3,4,5,6,7,8,9,10,J,Q,K]
#2) Calcolare il punteggio utilizzando un dizionario
#che associ ad ogni carta il suo valore

import random

mazzo=["1","2","3","4","5","6","7","8","9","10","J","K","Q"]
valore={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"K":10,"Q":10}

punteggio=0

carte_estratte=random.sample(mazzo,3)
    
#oppure
#for i in range (0,3):
#indice= random.randint(1,13)
#carta_estratta=mazzo[indice]

for i in range (0,3):
    punteggio=punteggio+valore[carte_estratte[i]]

