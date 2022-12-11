import random

EgyHet = []


for x in range(12):
    edzesek = []
    for y in range(7):
        edzesek.append(random.randint(1,10))
    EgyHet.append(edzesek)



i = 0
while i < len(edzesek):
    if i % 4 == 0:
        print(f"\n{i // 4 + 1}.hónap:")
    print(f"\n{i + 1}.hét: {edzesek[i]}")
    i += 1


volt = False
i = 0
while i < len(edzesek):
    j = 0
    while j < len(edzesek[i]):
        if edzesek[i][j] == 7:
            volt = True
            break
        j += 1
    if volt:
        break
    i += 1
napok = ("hetfo", "kedd","szerda", "csitortok", "pentek","szombat","vasarnap")

if volt:
    print(f"Az első 7km-es edzes napja: {i + 1}.het,{napok[j]} ")
else:
    print("nincs a feltetelnek megfelelo elem")

