#Dato un insieme di 20 punti su un piano cartesiano,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima o il punto con ordinata minima

import random

x=[]
y=[]

for i in range (0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))

#ascissa massima?
#scorrere la lista delle x, trovare il massimo e salvare l'indice
#visualizzare poi con una print il numero

massimo=x[0]
for i in range (0,20):
    if x[i]>massimo:
        massimo=x[i]
        indicemax=y[i]
print(massimo,indicemax)

minimo=y[0]
for i in range (0,20):
    if y[i]<minimo:
        minimo=y[i]
        indicemin=x[i]
print(indicemin,minimo)