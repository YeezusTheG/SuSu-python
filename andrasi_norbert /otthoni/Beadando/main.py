from definitions import *
import time
with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /otthoni/Beadando/input.txt","r") as f:
    numbers = []
    for x in f.read().split():
        if x.isnumeric():
            numbers.append(int(x))
    #A program csak az int-eket fogja elfogadni a beolvasásnál
while True:
    print("Menüpontok:\n1.Számok összege\n2.Számok számtani közepe\n3.Számok mértani közepe\n4.Számok négyzetes közepe\n5.Számok harmonikus közepe\n6.Számok módusza\n7.Számok mediánja\n0.Kilépés")
    choice = int(input("Adja meg a menüpont számjelét: "))
    time.sleep(1)
    if choice == 0:
        print("Kilépés...")
        time.sleep(3)
        break
    elif choice == 1:
        print("Számok összege: ",sum(numbers))
        time.sleep(3)
    elif choice == 2:
        print("Számok számtani közepe: ", szamtani_kozep(numbers))
        time.sleep(3)
    elif choice == 3:
        print("Számok mértani közepe: ", mertani_kozep(numbers))
        time.sleep(3)
    elif choice == 4:
        print("Számok négyzetes közepe: ", negyzetes_kozep(numbers))
        time.sleep(3)
    elif choice == 5:
        print("Számok harmonikus közepe: ", harmonikus_kozep(numbers))
        time.sleep(3)
    elif choice == 6:
        try:
            print("Számok módusza: ",modusz(numbers))
            time.sleep(3)
        except:
            print("Nincs módusz")
            time.sleep(3)
    elif choice == 7:
        print("Számok mediánja: ", median(numbers))
        time.sleep(3)