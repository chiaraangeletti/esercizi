import random
import math
import matplotlib.pyplot as plt

def registra_temperature(dizionario):
    """
    Questa funzione riempe con 24 numeri randomici un dizionario contentente i giorni della settimana.

    :params dizionario: Dizionario contenente come valore chiave il giorno e come valore la lista.
    """
    for chiave in dizionario:
        for i in range(0,24):
            dizionario[chiave].append(random.randint(-3,20))
    return(dizionario)

def media_giornaliera(dizionario):
    """
    Questa funzione calcola la media di una distribuzione numerica
    
    :params dizionario: Dizionario contenente come valore chiave il giorno e come valore la lista.
    """
    media_temp=[]
    somma=0
    for chiave,valore in dizionario.items():
        for elemento in valore:
            somma=somma+elemento
        media=somma/len(valore)
        media=round(media,1)
        media_temp.append(media)
    print("Le medie sono: "+str(media_temp))
    return(media_temp)

def varianza(dizionario,media_temp):
    """
    Questa funzione calcola la varianza di una distribuzione numerica data la lista delle medie
    
    :params dizionario: Dizionario contenente come valore chiave il giorno e come valore la lista.
    :params media_temp: Lista contenente la media di ogni giorno della settimana.
    """
    varianza_temp=[]
    giorno = 0
    for chiave,valore in dizionario.items():
        somma=0
        for elemento in valore:
            somma=somma+((elemento-media_temp[giorno])**2)
        varianza=somma/(len(valore)-1)
        varianza=round(varianza,1)
        varianza_temp.append(varianza)
        giorno = giorno +1
    print("Le varianze sono: "+str(varianza_temp))
    return(varianza_temp)
    
def giornata_calda_fredda(media_temp):
    """
    Questa funzione calcola la giornata più fredda e quella più calda della settimana in base alla media delle temperature.

    :params media_temp: Lista contenente la media di ogni giorno della settimana.
    """
    giornata_calda=media_temp[0]
    giornata_fredda=media_temp[0]
    gClado=0
    gFreddo=0
    giorni=["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"]
    for i in range(0,len(media_temp)):
        if media_temp[i]>giornata_calda:
            gCaldo=i
            giornata_calda=media_temp[i]
        elif media_temp[i]<giornata_fredda:
            gFreddo=i
            giornata_fredda=media_temp[i]
    print("La giornata più calda è "+str(giorni[gCaldo])+" con "+str(giornata_calda)+" gradi.")
    print("La giornata più fredda è "+str(giorni[gFreddo])+" con "+str(giornata_fredda)+" gradi.")
    
def deviazione_standard(varianza_temp):
    """
    Questa funzione calcola la deviazione standard di ogni giorno

    :params varianza_temp: Lista contenente la varianza di ogni giorno della settimana.
    """
    deviazioni=[]
    for elemento in varianza_temp:
        deviazione=math.sqrt(elemento)
        deviazione=round(deviazione,1)
        deviazioni.append(deviazione)
    print("le deviazioni standard sono: "+str(deviazioni))
    return(deviazioni)

def moda(dizionario):
    """
    Questa funzione calcola la moda delle temperature di ogni giorno

    :params dizionario: Dizionario contenente come valore chiave il giorno e come valore la lista.
    """
    nModa=0
    moda=0
    for chiave,valore in dizionario.items():
        for elemento in valore:
            volte=valore.count(elemento)
            if volte>nModa:
                nModa=volte
                moda=elemento
    print("La moda è "+str(moda)+".")
                
def errore_standard(deviazioni):
    """
    Questa funzione calcola l'errore standard delle temperature di ogni giorno

    :params deviazioni: Lista contenente le deviazioni standard di ogni giorno della settimana.
    """
    errori=[]
    nRilevazioni=24
    radiceRilev=math.sqrt(nRilevazioni)
    for elemento in deviazioni:
        errore=elemento/radiceRilev
        errore=round(errore,1)
        errori.append(errore)
    print("Gli errori standard sono: "+str(errori))
    
def crea_istogramma(dati, num_bins=10, titolo="Istogramma", colore="skyblue"):
    """
    Crea e visualizza un istogramma a partire da una lista o array di numeri.
    
    :param dati: Lista o array di valori numerici
    :param num_bins: Numero di intervalli (bins) dell'istogramma
    :param titolo: Titolo del grafico
    :param colore: Colore delle barre
    """
    plt.figure(figsize=(8, 5))
    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)
    plt.title(titolo)
    plt.xlabel("Valori")
    plt.ylabel("Frequenza")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


