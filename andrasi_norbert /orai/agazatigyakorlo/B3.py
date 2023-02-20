
def adatokBeolvasasa(fajlnev):
    adatok = {}
    with open("andrasi_norbert //orai//agazatigyakorlo//fuvarok.txt") as f:
        for sor in f:
            sor = sor.strip().split()
            rendszam = sor[0]
            kilometerszamok = [int(x) for x in sor[1:]]
            adatok[rendszam] = kilometerszamok
    return adatok

