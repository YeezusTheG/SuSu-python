
"""
with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /orai/20221215/text.txt") as f:
    for i in f:
        print(i)
"""

f = open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /orai/20221215/text.txt")
tmp = 1
for i in f:
    if tmp == 1:
        tmp = i

print(tmp)
for i in tmp:
    l=tmp.split(" ")
    print(l)

f.close()