#Analisi delle temperature settimanali.
#Una stazione meteo ha registrato le temperature (°C) di ogni ora per 7 giorni.
#Devi calcolare statistiche giornaliere e trovare la giornata più calda e più fredda della settimana.
#Struttura dati: lista di liste (7 giorni x 24 ore)

import random

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
    print(media_temp)
    
def varianza(dizionario, media_temp):
    varianza_temp=[]
    somma=0
    for chiave,valore in dizionario.items():
        for elemento in media_temp:
            somma=somma+((valore-elemento)**2)
        varianza=somma/len(valore)
        varianza=round(varianza,1)
        varianza_temp.append(varianza)
    print(varianza_temp)

if __name__ =="__main__":
    temperature={"Lunedì":[],"Martedì":[], "Mercoledì":[], "Giovedì":[], "Venerdì": [], "Sabato": [], "Domenica":[]}
    registra_temperature(temperature)
#    print(temperature)
    media_giornaliera(temperature)
    varianza(temperature,media_giornaliera)