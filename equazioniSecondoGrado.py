#Scrivere un programma per il calcolo delle soluzioni di un'equazione
#di secondo grado.

acquisisciCoefficienti()
if a!=0:
    calcolaDelta()
    visualizzaSoluzioni()
else:
    risolviEqazPrimoGrado
    
def acquisisciCoefficienti():
    a=input("Inserire il primo coefficiente: ")
    a=float(a)
    b=input("Inserire il secondo coefficiente: ")
    b=float(b)
    c=input("Inserire il terzo coefficiente: ")
    c=float(c)
    
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


