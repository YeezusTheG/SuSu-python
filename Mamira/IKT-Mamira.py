import random
from statistics import harmonic_mean
"""
lista = []
for i in range(7):
    x = random.randint(0,35)
    lista.append(x)
print(lista)
print("ennyi km-t futott összesen",sum(lista))
piheno = 0
j = 0
while j < len(lista):
    if 0 == lista[j]:
        piheno+=1
    j += 1
print("Ennyit napot pihent az elso héten: ",piheno)
"""
haromhetadata = []
for i in range(21):
    x = random.randint(0,35)
    haromhetadata.append(x)
print(f"Ennyit futott naponta: {haromhetadata}")
elsohet = []
i = 0
while i < len(haromhetadata)/ 7:
    j = 0
    print(f"{i+1}.hét: ",end="")

    while j < 7:
        print(haromhetadata[i*7+j], end=" ")
        j+=1
    print()
    i+=1