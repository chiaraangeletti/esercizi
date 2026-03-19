#Esercizio 2 verifica.
def massa_molare(formula):
    if formula == "H2O":
        return 18
    if formula == "NaCl":
        return 58.5
    if formula == "CO2":
        return 44
    return 0

def moli_da_massa(massa_g, formula, unita="g"):
    moli=massa_g/massa_molare(formula)
    return(moli)

def massa_da_moli(moli, formula):
    massa_g=moli*massa_molare(formula)
    return(massa_g)

def stampa_confronto(fUno, fDue, mUno, mDue):
    moliUno=moli_da_massa(mUno, fUno)
    moliDue=moli_da_massa(mDue, fDue)
    if moliUno>moliDue:
        print(fUno+" ha più moli.")
        diff=moliUno-moliDue
        print("La differenza delle moli è: "+str(diff))
    else:
        print(fDue+" ha più moli.")
        diff=moliDue-moliUno
        print("La differenza delle moli è: "+str(diff))

if __name__ =="__main__":
    formulaUno="H2O"
    massa=90
    nMoli=moli_da_massa(massa,formulaUno)
    print(nMoli)
    formulaDue="CO2"
    moli=1.5
    grammi=massa_da_moli(moli, formulaDue)
    print(grammi)
    stampa_confronto(formulaUno, formulaDue, massa, grammi)