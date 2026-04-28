#Analisi delle temperature settimanali.
#Una stazione meteo ha registrato le temperature (°C) di ogni ora per 7 giorni.
#Devi calcolare statistiche giornaliere e trovare la giornata più calda e più fredda della settimana.
#Struttura dati: lista di liste (7 giorni x 24 ore)

import random
import math
import matplotlib.pyplot as plt
from analisi_dati import *

def registra_temperature(dizionario):
    for chiave in dizionario:
        for i in range(0,24):
            dizionario[chiave].append(random.randint(-3,20))
    return(dizionario)

def media_giornaliera(dizionario):
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
    deviazioni=[]
    for elemento in varianza_temp:
        deviazione=math.sqrt(elemento)
        deviazione=round(deviazione,1)
        deviazioni.append(deviazione)
    print("le deviazioni standard sono: "+str(deviazioni))
    return(deviazioni)

def moda(dizionario):
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
    errori=[]
    nRilevazioni=24
    radiceRilev=math.sqrt(nRilevazioni)
    for elemento in deviazioni:
        errore=elemento/radiceRilev
        errore=round(errore,1)
        errori.append(errore)
    print("Gli errori standard sono: "+str(errori))
    
def covarianza(dizionario,giornoUno,giornoDue,media_temp):
    media_x=media_temp[0]
    media_y=media_temp[1]
    chiave_x=dizionario[giornoUno]
    chiave_y=dizionario[giornoDue]
    n=len(chiave_x)
    somma_prodotti_scarti=0
    for i in range(n):
        scarto_x = chiave_x[i]-media_x
        scarto_y = chiave_y[i]-media_y
        somma_prodotti_scarti = somma_prodotti_scarti + (scarto_x * scarto_y)
    covarianza=somma_prodotti_scarti/(n-1)
    covarianza=round(covarianza,1)
    print("La covarianza è: "+str(covarianza))
    if covarianza<0:
        print("Al crescere delle temperature del primo giorno, decrescono le temperature del secondo.")
    else:
        print("Al crescere delle temperature del primo giorno, crescono anche le temperature del secondo.")
    return(covarianza)
    

if __name__ =="__main__":
    temperature={"Lunedì":[],"Martedì":[], "Mercoledì":[], "Giovedì":[], "Venerdì": [], "Sabato": [], "Domenica":[]}
    registra_temperature(temperature)
    medie = media_giornaliera(temperature)
    lVarianze=varianza(temperature,medie)
    giornata_calda_fredda(medie)
    lDeviazioni=deviazione_standard(lVarianze)
    moda(temperature)
    errore_standard(lDeviazioni)
#    crea_istogramma(temperature["Lunedì"])
    covarianza_L_M=covarianza(temperature,"Lunedì","Martedì",medie)
    covarianza_M_M=covarianza(temperature,"Martedì","Mercoledì",medie)
    covarianza_M_G=covarianza(temperature,"Mercoledì","Giovedì",medie)
    covarianza_G_V=covarianza(temperature,"Giovedì","Venerdì",medie)
    covarianza_V_S=covarianza(temperature,"Venerdì","Sabato",medie)
    covarianza_S_D=covarianza(temperature,"Sabato","Domenica",medie)