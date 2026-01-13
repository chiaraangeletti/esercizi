def modifica_numero (n):
    n=n+10
    
def modifica_lista (lista):
    lista.append(10)
    
x=5
numeri=[1,2,3]
modifica_numero(x)
modifica_lista(numeri)

#x viene passato per valore nella funzione quindi se non c'è un return, x rimane invariato mentre una lista viene
#passata per riferimento quindi viene modificata all'interno della funzione.