def T (i):
    #Barmi amit megfogunk adni feltetelnek
    return i
#Összegzés
def osszegzestetel(X):
    s = 0
    for i in range(len(X)):
        s = s + X[i]
    return s

#Megszámolás
def megszamolastetel(X):
    c = 0
    for i in range(len(X)):
        if T(X[i]):
            c += 1
    return c
#Maximum-kiválasztás
def MaxKivalasztas(X):
    MaxErt = X[0]
    MaxInd = 0
    for i in range(1, len(X)):
        if X[i] > MaxErt:
            MaxErt = X[i]
            MaxInd = i
    return(MaxErt,MaxInd)
#Keresés
def kereses (X):
    i = 1
    while i <= len(X) and not T(X[i]):
        i += 1
    Van = i <= len(X)
    if Van:
        Index = i
        Ertek = X[i]
    return(Index, Ertek)

#Eldőntés
def eldontes (X):
    i = 1
    while i <= len(X) and not T(X[i]):
        i += 1
    Van = i <= len(X)
    return Van

#Kiválasztás
def kivalasztas (X):
    i = 1
    while not T(X[i]):
        i += 1
    Index = i
    Ertek = X[i]
    return(Index, Ertek)