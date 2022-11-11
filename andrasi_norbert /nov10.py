A = [1,2,3,4,5,6,7,8,9]
B = 8
C = []
def T(a,i):
    global masikszam
    for i in range(len(A)):
        if a*A[i]==B:
            masikszam = A[i]
            return True
i = 0
while i < len(A) and not T(A[i]):
    i = i + 1
van = i < len(A)
if van:
    print("A két szám:  ", (A[i]), "és" (masikszam) )
else:
    print("nincs a listában a tételnek megfelelő 2 elem")