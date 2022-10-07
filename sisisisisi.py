import random
lista = []
lista2 =[]
also = random.randint(1,3)
felso = random.randint(6,9)
for i in range(10):
    szam = random.randint(also,felso)
    lista.append(szam)
for i in range(len(lista)):
    if lista[i] == felso:
        lista2.append(i)

print(also)
print(felso)
print(lista)
print(lista2)

