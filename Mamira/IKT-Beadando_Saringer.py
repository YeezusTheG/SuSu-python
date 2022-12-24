import random
# 1. Feladat
halak = []
for i in range(3): # 3 hónapot vizsgálunk                                       # a pingivnek 3 hónap alatti napi halfogyasztása
    hetek = []
    halak.append(hetek)
    for j in range(4): # 4x fut le mivel 4 hét van egy hónapban
        napok = []
        hetek.append(napok)
        for k in range(7): # 7x fut le mivel a hét minden napján ettek halat
            pingvinek = []
            napok.append(pingvinek)
            for o in range(4): # 4db pingvin (Kapitány, Kowalski, Rico, Közlegény)
                pingvinek.append(random.randint(1,5))

# 2. Feladat
i = 0
while i <= len(halak) and not kereses(halak[i]):
    i = i + 1
Van = i <=len(halak)
if Van:
    Ind = i
    Ert = halak[i]


# 3. Feladat
MaxErt = halak[1]