import numpy as np

# Fájl megnyitása olvasásra
with open("Mamira//IKT_Beadando_Saringer//matrix.txt", "r") as f:
    # Adatok beolvasása NumPy tömbbe
    matrix = np.loadtxt(f, dtype=int)

# A mátrix kiíratása
for i in range(matrix.shape[0]):
    row_str = f"{i+1}. sor:"
    for j in range(matrix.shape[1]):
        row_str += f" {matrix[i,j]}"
    print(row_str)

print()
# Sorok összege
for i in range(matrix.shape[0]):
    row_sum = sum(matrix[i])
    print(f"{i+1}. sor osszege: {row_sum}")

print()
# Oszlopok összege
for j in range(matrix.shape[1]):
    col_sum = sum(matrix[:,j])
    print(f"{j+1}. oszlop osszege: {col_sum}")

print()

# Legnagyobb és legkisebb szám meghatározása
min_val = matrix.min()
max_val = matrix.max()

# Legnagyobb és legkisebb szám pozíciójának meghatározása
min_pos = np.where(matrix == min_val)
max_pos = np.where(matrix == max_val)

# Kiíratás
print(f"A legkisebb szám: {min_val}, a legkisebb szám pozíciója: ({min_pos[0][0]+1}, {min_pos[1][0]+1})")
print(f"A legnagyobb szám: {max_val}, a legnagyobb szám pozíciója: ({max_pos[0][0]+1}, {max_pos[1][0]+1})")

print()

# Felhasználói input kérés és ellenőrzés
while True:
    x = input("Kérem adjon meg egy -9 és 9 közötti egész számot: ")
    if x.isdigit() and -9 <= int(x) <= 9:
        x = int(x)
        break
    else:
        print("Hibás input! Kérem adjon meg egy -9 és 9 közötti egész számot.")

# A megadott szám előfordulásának keresése
diag_count = 0
lower_count = 0
upper_count = 0

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i,j] == x:
            if i == j:
                diag_count += 1
            elif i > j:
                lower_count += 1
            else:
                upper_count += 1

# Eredmény kiíratása
print(f"{x} szerepel {diag_count} alkalommal az átlóban, {lower_count} alkalommal az alsó háromszögben, és {upper_count} alkalommal a felső háromszögben.")
