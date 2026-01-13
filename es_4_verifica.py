def aggiorna (valore,lista,fattore=2):
    valore=valore*fattore
    lista.append(valore)
    return valore
x=3
dati=[1,2]
ris1=aggiorna(x,dati)
ris2=aggiorna(x,dati,3)