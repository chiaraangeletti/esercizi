#Costruzione di una classe che disegni un atomo
class Atomo:
    def __init__(self, simbolo, numeroAtomico, massa):
        self.simbolo=simbolo
        if numeroAtomico<0:
            raise ValueError("Il numero atomico deve essere positivo") #il programma da errore se non rispetta la condizione
        else:
            self.numeroAtomico=numeroAtomico
        self.massa=massa
        protoni=numeroAtomico
        massaDue=round(massa)
        neutroni=massaDue-numeroAtomico
        rapporto=neutroni/numeroAtomico
        if rapporto>=0.9 and rapporto<=1.6:
            print("L'atomo è stabile")
        else:
            print("L'atomo è instabile")
        
        
primo_elemento=Atomo("Fe", 26, 55.84)
try:
    secondo_elemento=Atomo("H", 1, 1.008)
except ValueError:
    print("Il numero atomico deve essere positivo")