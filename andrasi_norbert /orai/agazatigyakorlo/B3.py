
def adatokBeolvasasa(fajlnev):
    with open(fajlnev, "r") as f:
        adatok = []
        for sor in f:
            sor = sor.strip().split()
            rendszam = sor[0]
            futasteljesitmenyek = []
            for i in range(1, len(sor)):
                try:
                    futasteljesitmenyek.append(int(sor[i]))
                except ValueError:
                    futasteljesitmenyek.append(0)
            adatok.append([rendszam] + futasteljesitmenyek)
    return adatok

def nullaKm(lista):
    nullak_szama = 0
    for row in lista:
        for elem in row[1:]:
            if elem == 0:
                nullak_szama += 1
    return nullak_szama



adatok = adatokBeolvasasa("andrasi_norbert //orai//agazatigyakorlo//fuvarok.txt")
print(adatok)
nullak_szama = nullaKm(adatok)
print(f"Az adatbázisban {nullak_szama}db 0 km havi futásteljesítményt tartalmazó hónap van.")