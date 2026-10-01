#Analisi del profilo genetico

class CampioneDNA:
    """
    Classe per rappresentare e apportare modifiche su un campione di DNA.
    """
    def __init__(self, codice_campione, sequenza, laboratorio, geni_mappati=[], mutazioni_rilevate={}):
        """
        Inizializza il campione di DNA con dei parametri:
        codice_campione(str): identifica il campione
        sequenza(str): sequenza nucleotidica
        laboratorio(str): nome del laboratorio
        geni_mappati(list, opzionale): lista dei geni identificati
        mutazioni_rilevate(dict, opzionale): mappa delle mutazioni
        """
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza.upper() #viene convertita in maiuscolo
        self.laboratorio = laboratorio
        self.__geni_mappati=geni_mappati
        self.__mutazioni_rilevate = mutazioni_rilevate
        
        #parametri opzionali: se non vengono dati vengono dati per vuoti
        """
        if geni_mappati is None:
            self.__geni_mappati = []
        else:
            self.__geni_mappati = geni_mappati
        
        if mutazioni_rilevate is None:
            self.__mutazioni_rilevate = {}
        else:
            self.__mutazioni_rilevate = mutazioni_rilevate
        """

    def aggiungi_gene(self, gene):
        """
        Aggiunge un gene all'interno della lista dei geni identificati se questo non è già presente.
        """
        if gene not in self.__geni_mappati:
            self.__geni_mappati.append(gene)
            
    def registra_mutazione(self, posizione, tipo_mutazione):
        """
        Aggiunge il tipo di mutazione in una certa posizione all'interno della mappa delle mutazioni.
        """
        self.__mutazioni_rilevate[posizione] = tipo_mutazione
       
    def calcola_percentuale_gc(self):
        """
        Calcola e restituisce la percentuale delle basi G e C nella sequenza nucleotidica.
        Ritorna:
        percentuale(float): percentuale di basi GC rispetto alla lunghezza totale della sequenza
        """
        if len(self.__sequenza) == 0:
            return 0.0
        conteggio_gc = 0
        for base in self.__sequenza:
            if base == "G" or base== "C":
                conteggio_gc = conteggio_gc + 1
        percentuale = (conteggio_gc / len(self.__sequenza)) * 100
        return percentuale
    def stampa_report(self):
        if len(self.__sequenza) > 20:
            seq_mostrata = self.__sequenza[:20] + "..."
        else:
            seq_mostrata = self.__sequenza
            print("=== REPORT CAMPIONE DNA ===")
            print("Codice:", self.__codice_campione)
            print("Laboratorio:", self.laboratorio)
            print("Sequenza:", seq_mostrata)
            print("Geni mappati:", self.__geni_mappati)
            print("Mutazioni rilevate:", self.__mutazioni_rilevate)
            print("Percentuale GC:", self.calcola_percentuale_gc(), "%")