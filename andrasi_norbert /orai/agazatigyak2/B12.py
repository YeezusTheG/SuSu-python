import random
szamok = []
while True:
    size = input("Add meg a lista méretét [5...25]: ")
    try:
        size = int(size)
        if size < 26 and size > 4:
            break
        else:
            print("Hibás adatbevitel! Próbáld újra!")
    except:
        print("Hibás adatbevitel! Próbáld újra!")
for i in range(size):
    szamok.append(random.randint(-10,10))
print(f"A lista tartalma: {szamok}")

#2.Feladat

c = 0
for i in szamok:
    if i == 0:
        c = c + 1
d = 0
for i in szamok:
    if i < 0:
        d = d + 1
print(f"A listában lévő elemek összege: {sum(szamok)}")
print(f"A listában lévő 0 elemek száma: {c}")
print(f"A listában lévő negatív elemek száma: {d}")
if c < d:
    print("Nem igaz az állítás!")
else:
    print("Igaz az állítás!")
