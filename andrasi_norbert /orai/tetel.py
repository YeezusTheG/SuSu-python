#Összegzés
def osszegzes(X, func,s=0):
    for i in range(len(X)):
        s = func(X[i])
    return s

#Megszámolás
def megszamolas(X, T):
    c = 0
    for i in range(len(X)):
        if (T(X[i])):
            c += 1
    return c

#szelsoertek
def szelsoertek(X, func):
    Ert = X[0]
    Ind = 0
    for i in range(1, len(X)):
        if (func(X[i],Ert)):
            Ert = X[i]
            Ind = i
    return(Ert,Ind)

#Keresés
def kereses (X, func):
    i = 1
    while i <= len(X) and not func(X[i]):
        i += 1
    Van = i <= len(X)
    if Van:
        Index = i
        Ertek = X[i]
    return(Index, Ertek)

#Eldőntés
def eldontes (X, func):
    i = 1
    while i <= len(X) and not func(X[i]):
        i += 1
    Van = i <= len(X)
    return Van

#Kiválasztás
def kivalasztas (X, func):
    i = 1
    while not func(X[i]):
        i += 1
    Index = i
    Ertek = X[i]
    return(Index, Ertek)