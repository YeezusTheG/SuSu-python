from saringer_beadando_fuggvenyek import *
while True:
    while True:
        print("Ön jelenleg a BASIC CALCULATOR 2000-et használja")
        print(" 1)Összeadás \n","2)Kivonás \n","3)Szorzás \n","4)Osztás \n","0)Kilépés")

        menupont = int(input("Adja meg a kívánt szolgátatás menüpontját!  "))

        if menupont > 4 or menupont < 0:
            print("Hibás Adatbevitel, próbálja újra")
        else:
            break
    if menupont == 0:
        print("Program bezárása...")
        break

    if menupont == 1:
        while True:
            x = input("Adja meg az összeadásra szánt első számot: ")
            y = input("Adja meg az összeadásra szánt második számot: ")
            try:
                x = float(x)
                y = float(y)
                break
            except:
                print("Nem számokat adott meg")
        print("Összeadás eredménye: ",osszeadas(x,y))
        print()

    if menupont == 2:
        while True:
            x = input("Adja meg az kivonásra szánt első számot: ")
            y = input("Adja meg az kivonásra szánt második számot: ")
            try:
                x = float(x)
                y = float(y)
                break
            except:
                print("Nem számokat adott meg")
        print("Kivonás eredménye: ", kivonas(x,y))
        print()

    if menupont == 3:
        while True:
            x = input("Adja meg az szorzásra szánt első számot: ")
            y = input("Adja meg az szorzásra szánt második számot: ")
            try:
                x = float(x)
                y = float(y)
                break
            except:
                print("Nem számokat adott meg")
        print("Szorzás eredménye: ", szorzas(x,y))
        print()

    if menupont == 4:
        while True:
            x = input("Adja meg az osztásra szánt első számot: ")
            y = input("Adja meg az osztásra szánt második számot: ")
            try:
                x = float(x)
                y = float(y)
                break
            except:
                print("Nem számokat adott meg")
        print("Osztás eredménye", osztas(x,y))
        print()