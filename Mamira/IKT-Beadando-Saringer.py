import random
def atlag(x):
    a = sum(x)/len(x)
    return a

osztaly = []


for i in range(30):
    osztaly.append(random.randint(1,5))

#1.Feladat
print(f"A dolgozat átlageredménye: {round(atlag(osztaly),2)}")

#2.Feladat
jegyek  = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for i in osztaly:
    jegyek[i] += 1

print()

print("Elégtelen (1): {} db".format(jegyek[1]))
print("Elégséges (2): {} db".format(jegyek[2]))
print("Közepes (3): {} db".format(jegyek[3]))
print("Jó (4): {} db".format(jegyek[4]))
print("Jeles (): {} db".format(jegyek[5]))

print()

#3.Feladat
for i in range(1,6):
    print("{}:{}".format(i, "*" * jegyek[i]))