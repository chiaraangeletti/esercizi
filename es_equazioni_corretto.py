#Scrivere un programma per il calcolo delle radici di un'equazione
#di secondo grado.

import math

def calcoloDelta(a,b,c):
    delta=(b*b)-(4*a*c)
    return(delta)

def controlloDelta(a,b,delta):
    if delta<0:
        print("L'equazione è impossibile.")
    elif delta==0:
        calcoloUnaRadice(a,b)
    else:
        calcoloDueRadici(a,b,delta)

def calcoloUnaRadice(a,b):
    soluzione=-b/2*a
    print(soluzione)
    
def calcoloDueRadici(a,b,delta):
    xUno=(-b+math.sqrt(delta))/2*a
    xDue=(-b-math.sqrt(delta))/2*a
    print(xUno,xDue)

if __name__=="__main__":
    a=input("Inserire il coefficiente a: ")
    a=float(a)
    b=input("Inserire il coefficiente b: ")
    b=float(b)
    c=input("Inserire il coefficiente c: ")
    c=float(c)
    delta=calcoloDelta(a,b,c)
    print(delta)
    controlloDelta(a,b,delta)
    