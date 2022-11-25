import random
"""
sor, oszlop = (6,4)
matrix = [[random.randint(1,5)]*sor]*oszlop
print(matrix)"""

matrix = []


for x in range(6):
    sor = []
    for y in range(4):
        sor.append(random.randint(1,5))
    matrix.append(sor)

print(matrix)