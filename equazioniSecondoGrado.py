#Scrivere un programma per il calcolo delle soluzioni di un'equazione
#di secondo grado.

def acquisisciCoefficienti(a,b,c):
    if a == 0:
        print("L'equazione è di primo grado.") 

def calcolaDelta(a,b,c):
    delta=b*b-4*a*c
    print(delta)

def visualizzaSoluzioni(delta):
    if delta<0:
        print("L'equazione non ammette soluzioni.")
    else:
        radice=math.sqrt(delta)
        xUno= -b-radice/(2*a)
        xDue= -b+radice/(2*a)
        print("xUno=",xUno, "xDue=",xDue)

def risolviEquazPrimoGrado(b,c):
    if b==0 and c==0:
        print("L'equazione è indeterminata.")
    elif b==0:
        print("L'equazione è impossibile.")
    else:
        x=-c/b

if __name__ == '__main__':
    coeffUno=input("Inserire il primo coefficiente: ")
    coeffUno=float(coeffUno)
    coeffDue=input("Inserire il secondo coefficiente: ")
    coeffDue=float(coeffDue)
    coeffTre=input("Inserire il terzo coefficiente: ")
    coeffTre=float(coeffTre)
    
