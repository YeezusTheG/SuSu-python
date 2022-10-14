import random
lista = []
for i in range(7):
    x = random.randint(0,35)
    lista.append(x)
print(lista)
print("ennyi km-t futott:",sum(lista))
piheno = 0
pihenonapok = []
j = 0
while j < len(lista):
    if piheno == lista[j]:
        pihenonapok.append(piheno)
    j += 1
print("Ennyit napot pihent: ",len(pihenonapok))