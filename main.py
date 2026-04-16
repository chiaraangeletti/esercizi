from analisi_dati import*

if __name__ =="__main__":
    temperature = {"Lunedì":[],"Martedì":[], "Mercoledì":[], "Giovedì":[], "Venerdì": [], "Sabato": [], "Domenica":[]}
    registra_temperature(temperature)
    medie = media_giornaliera(temperature)
    lVarianze = varianza(temperature,medie)
    giornata_calda_fredda(medie)
    lDeviazioni = deviazione_standard(lVarianze)
    moda(temperature)
    errore_standard(lDeviazioni)
    Istogramma = crea_istogramma()