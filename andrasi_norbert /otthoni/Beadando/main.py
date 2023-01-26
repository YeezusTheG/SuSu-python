from definitions import *
with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /otthoni/Beadando/input.txt","r") as f:
    numbers = []
    for x in f.read().split():
        if x.isnumeric():
            numbers.append(int(x))
    #A program csak az int-eket fogja elfogadni a beolvasásnál
print(numbers)