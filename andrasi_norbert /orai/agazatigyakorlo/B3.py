
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

def nullaKm(adatok):
    szamlalo = 0
    for i in adatok[1:]:
        if i == 0:
            szamlalo += 1
    return szamlalo


adatok = adatokBeolvasasa("andrasi_norbert //orai//agazatigyakorlo//fuvarok.txt")
print(adatok)
nullak_szama = nullaKm(adatok)
print(nullak_szama)