#Scrivere un programma che dati due punti in un piano
#cartesiano scriva l'equazione della retta associata
#e mandi in output il messaggio con con la positività
#o negatività del coefficiente angolare.
#1) m=y2-y1/x2-x1 Utilizziamo la funzione perché serve la restituzione di un valore.
#   I parametri sono 4: xUno, yUno, xDue, yDue.
#2) y-y0 = m*(x-x0) Utilizziamo la procedura perché è sufficiente scrivere l'equazione della retta.
#   I parametri sono m, xDue, yDue.

import random

def calcolo_m(xUno,yUno,xDue,yDue):
    m=(yDue-yUno)/(xDue-xUno)
    return(m) #Quando termina la funzione, muoiono tutte le variabili e viene ritornato un valore

def equazione(m,x,y):
    eq="y-"+str(y)+"="+str(m)+"(x-"+str(x)+")" #Concatenazione di stringje dove c'è una parte fissa e una parte variabile
    print(eq)
    
def controllo_m(m):
    if m>0:
        print("m ha segno positivo")
    elif m==0:
        print("m è nullo")
    else:
        print("m ha segno negativo")
        
def incrementoUno(a):
    a=a+1
    print(a)
    
def incremento_uno_stable(a):
    a=a+1
    return(a)

if __name__=="__main__":
    xUno=random.randint(-20,20)
    yUno=random.randint(-20,20)
    xDue=random.randint(-20,20)
    yDue=random.randint(-20,20)
    
    coefficiente_angolare=calcolo_m(xUno,yUno,xDue,yDue)
    print(coefficiente_angolare)
    equazione(coefficiente_angolare,xDue,yDue)
    controllo_m(coefficiente_angolare)
    incrementoUno(xUno) #xUno in questa funzione viene passato per valore quindi viene creata una copia ma xUno non cambia
    xUno=incremento_uno_stable(xUno) #Sovrascrivo la stessa variabile per cambiare il suo valore nel main.