korok = {}
with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /orai/20230119/input.txt") as f:
    for line in f:
        nevek, kor= line.strip().split()
        korok[nevek] = int(kor)

osszes_kor = sum(korok.values())
atlag = osszes_kor / len(korok)
closest_name = None
min_diff = None
for name in korok:
    kor = korok[name]
    diff = abs(kor - atlag)
    if min_diff is None or diff < min_diff:
        min_diff = diff
        closest_name = name
print(atlag , closest_name)