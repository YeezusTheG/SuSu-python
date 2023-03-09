def adatokBeolvasasa(file):
    f = open(file, "r")
    adatok = []
    adatok = [line.split() for line in f]
    f.close()
    return adatok

matrix = adatokBeolvasasa("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /orai/agazatigyak2/selejt.txt")

print(matrix)

new_matrix = []
for i in matrix:
    newlist = []
    for k in i:
        newlist.append(int(k))
    new_matrix.append(newlist)
print(new_matrix)


def hatekonysag(list):
    for i in list:
        i = 0
        while i <= len(list) and not i != 0:
        i += 1
    Van = i <= len(list)
    if Van:
        c += 1
    return 
print(f"Hatékony napok száma: {hatekonysag(new_matrix)}")