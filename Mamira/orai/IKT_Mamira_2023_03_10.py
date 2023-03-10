def adatokBeolvasasa(file):
    d = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip().split()
            d[line[0]] = list(map(int, line[1::]))
    return d



eladasok = adatokBeolvasasa("/home/markali/Dokumentumok/GitHub/SuSu-python/Mamira/orai/input.txt")


print(eladasok)


for key, value in eladasok.items():
    print(key, ':', sum(value))