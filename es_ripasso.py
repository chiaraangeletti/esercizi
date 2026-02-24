#Scheda 1 esercizio 1
numeri=[1,2,3,4,5]
print(numeri[2])
#Scheda 1 esercizio 2
numeri[1]=10
print(numeri)
#Scheda 1 esercizio 3
numeri.append(6)
print(numeri)
#Scheda 1 esercizio 4
lista=["Ksenia","Sara","Sofia",4,5]
print(lista[len(lista)-1])

#Scheda 2 esercizio 1
colori=["rosso", "blu", "verde", "giallo", "nero"]
print(colori[0:2])
#Scheda 2 esercizio 2
print(colori[2:])
#Scheda 2 esercizio 3
colori.insert(1,"bianco")
print(colori)
#Scheda 2 esercizio 4
colori.remove("verde")
print(len(lista))

#Scheda 3 esercizio 1
for i in range(10):  
    print(i)
#print(list(range(5))) #[0,1,2,3,4]
#Scheda 3 esercizio 2
for i in range(5,16):
    print(i)
#print(list(range(0,7))) #[0,1,2,3,4,5,6]
#Scheda 3 esercizio 3
for i in range(0,31,3):
    print(i)
#print(list(range(0,7,2))) #[0,2,4,6]
#Scheda 3 esercizio 4
for i in range(0,8):
    print("Ciao")
    
#Scheda 4 esercizio 1
città = ["Roma", "Milano", "Napoli", "Torino"]
for i in range(0,len(città)):
    print(f"Città all'indice{i}:{città[i]}")