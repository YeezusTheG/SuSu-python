rendszamok = []
adatok = []


def adatokBeolvasasa(
    f = open("andrasi_norbert //orai//agazatigyakorlo//fuvarok.txt")
    sorok = f.readlines()
    f.close()
    for i in sorok:
        rendszamok.append(i[0])
        adat = []
        for j in range(1,len(i)):
            adat.append(j)
        adatok.append(adat)
)