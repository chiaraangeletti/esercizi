#Dato un insieme di 20 punti su un piano cartesiano,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima o il punto con ordinata minima

import random

x=[]
y=[]

for i in range (0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))

punti_cartesiano=[]

for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
#Come accedere alla x del primo punto? Il primo 0 rappresenta la coppia
#il secondo 0 rappresenta il numero all'interno della coppia
    
print(punti_cartesiano[0][0])

#Come accedere alla y del primo punto?

print(punti_cartesiano[0][1])