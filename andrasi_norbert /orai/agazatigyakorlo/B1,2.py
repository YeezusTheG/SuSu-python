import random

#1.Feladat

while True:
    size = input("Add meg a lista méretét [10...20]: ")
    try:
        size = int(size)
        if size < 21 and size > 9:
            break
        else:
            print("Hibás adatbevitel! Próbáld újra!")
    except:
        print("Hibás adatbevitel! Próbáld újra!")


elemek = []

for i in range(size):
    elemek.append(random.randint(1,5))
print("A lista tartalma:",elemek)

#2.Feladat

print("A listában lévő számok összege:", sum(elemek))

MaxErtek = elemek[0]
MaxIndex = 0
for i in range(len(elemek)):
    if elemek[i] > MaxErtek:
        MaxErtek = elemek[i]
        MaxIndex = i
print(f"A lista legnagyobb elem: {MaxErtek}, helye: {MaxIndex + 1}.pozíció")