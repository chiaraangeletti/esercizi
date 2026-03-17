#Esercizio 3 verifica.
def aggiungi_voto(registro, voto):
    registro.append(voto)
    print(registro)

def media_registro(registro, arrotonda_a=0):
    somma=0
    for voto in registro:
        somma=somma+voto
    media=somma/len(registro)
    media=round(media,arrotonda_a)
    return(media)

def voti_sufficienti(registro):
    solosuff=[]
    for i in range(0,len(registro)):
        if registro[i]>=6:
            solosuff.append(registro[i])
    return(solosuff)

def stampa_esito(registro):
    for voto in registro:
        if voto>=6:
            print("Sufficiente.")
        else:
            print("Insufficiente - Recupera!")

if __name__ =="__main__":
    classe=[6,7,5,8]
    aggiungi_voto(classe,9)
    print(media_registro(classe, arrotonda_a=1))
    #Oppure
    #media-del_registro=media_registro(arrotonda_a=1, registro=classe)
    #Oppure
    #media_del_registro=media_registro(classe, arrotonda_a=1)
    #print(media_del_registro)
    sufficienze=voti_sufficienti(classe)
    print(sufficienze)
    stampa_esito(classe)