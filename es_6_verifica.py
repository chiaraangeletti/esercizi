#Scrivere una funzione conta_maggiori che riceve una lista di numeri e una soglia che riceve
#una lista di numeri e una soglia (valore predefinito=0)
#e restituisce quanti numeri sono maggiori della soglia

#def conta_maggiori (lista,soglia=0):
#    contatore=0
#   for i in range (0,len(lista)):
#        if lista[i]>soglia:
#           contatore=contatore+1
#    return(contatore)

listaNumeri=[-1,-2,3,4,5]
maggiori=conta_maggiori(listaNumeri)
minori=conta_maggiori(listaNumeri,4)

def conta_maggiori (lista,soglia=0):
    contatore=0
    for elemento in lista:
        if elemento>soglia:
            contatore=contatore+1
    return(contatore)