def nev(x):
    print(x)
nev("asd")
nev(9)
nev(7+2)

def osszegzestetel(X):
    s = 0
    for i in range(len(X)):
        s = s + X[i]
    return s

l = [3,5,5,6,5,6]

g = osszegzestetel(l)
print(g)


def megszamolas(X):
    c = 0
    for i in range(len(X)):
        if i == "a":
            c += 1
    return c

def maxkivalasztas(X):
    MaxErt = X[0]
    MaxInd = 0
    for i in range(1, len(X)):
        if X[i] > MaxErt:
            MaxErt = X[i]
            MaxInd = i
    return(MaxErt,MaxInd)

def T(a):
    a == "a"
    return(a)
def kereses(X,):
    i = 0
    while i <= len(X) and not T(X[i]):
        i = i + 1
    Van = i <= len(X)
    if Van:
        Ertek = X[i]
        Ind = i

