def adatokBeolvasasa(file):
    d = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip().split()
            d[line[0]] = list(map(int, line[1::]))
    return d



eladasok = adatokBeolvasasa("/home/markali/Dokumentumok/GitHub/SuSu-python/Mamira/orai/input.txt")


print(eladasok)
maxeladas = []

for key, value in eladasok.items():
    maxeladas.append(sum(value))
    print(key, ':', sum(value))


print(maxeladas)

MaxErtek = maxeladas[0]
MaxIndex = 0
for i in range(len(maxeladas)):
    if (maxeladas[i] >= MaxErtek):
        MaxErtek == maxeladas[i]
        MaxIndex == i

print(MaxErtek,MaxIndex)
