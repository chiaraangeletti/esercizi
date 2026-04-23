#Correzione esercizio 2 verifica.

#Lettura dei file
def letturaFile(nome_file):
    dati=[]
    with open (nome_file) as f:
        for line in f:
            ph = line.strip("\n")
            dati.append(float(ph))
    return(dati)

#Funzione calcola la media
def media(lista):
    somma=0
    media=0
    for i in range (len(lista)):
        somma=lista[i]+somma
    media=somma/len(lista)
    return(media)

#Funzione confronto medie
def confrontaMedie(mediaUno,mediaDue):
    if mediaUno>mediaDue:
        differenza=mediaUno-mediaDue
        print("La differenza tra le medie è: "+str(differenza))
    else:
        differenza=mediaDue-mediaUno
        print("La differenza tra le medie è: "+str(differenza))
        


if __name__=="main":
    terreno=letturaFile("terreno.csv")
    print(terreno)
    senza_terreno=letturaFile("senza_terreno.csv")
    print(senza_terreno)
    media_terreno=media(terreno)
    media_senzaterreno=media(senza_terreno)
    confrontaMedie(media_terreno,media_senzaterreno)