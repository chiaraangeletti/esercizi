#Esercizio 1 verifica.
g = 9.81 # m/s²

def posizione(t, v0=0, a=g, s0=0):
    s=s0 + v0*t + 0.5*a*t**2
    s=round(s,1)
    return(s)

def velocita(t, v0=0, a=g):
    v=v0+a*t
    v=round(v,1)
    return(v)

def tempi_posizioni(tempi,posizioni):
    for i in tempi:
        posiz=posizione(i)
        posizioni.append(posiz)
        
def arrotonda_decimali(lista):
    for i in range(0,len(lista)):
        lista[i]=round(lista[i],2)
        lista.append(lista[i])

if __name__ =="__main__":
    t=4
    v0=5
    posizioneUno=posizione(t)
    print(posizioneUno)
    velocitaUno=velocita(t, v0)
    print(velocitaUno)
    tempi=[1.4,3.5,5.2,9.3]
    posizioni=[]
    tempi_posizioni(tempi, posizioni)
    arrotonda_decimali(posizioni)
    print(posizioni)