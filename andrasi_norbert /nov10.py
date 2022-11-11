A = [1,2,3,4,5,6,7,8,9]
B = 8
C = []
def T(szam):
    for i in range(len(A)):
        if szam*A[i]==B and szam != A[i]:
            global found_num
            found_num = A[i]
            return True
i = 0
while i < len(A) and not T(A[i]):
    i = i + 1
van = i < len(A)
if van:
    print(f"A két szám: {A[i]} és {found_num}")
else:
    print("nincs a listában a tételnek megfelelő 2 elem")