letters = ["A","Á","B","C","D","E","É","F","G","H","I","Í","J","K","L","M","N","O","Ó","Ö","Ő","P","Q","R","S","T","U","Ú","Ü","Ű","V","W","X","Y","Z"]
lowerletters = ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","ö","ő","p","q","r","s","t","u","ú","ü","ű","v","w","x","y","z"]
print(lowerletters)
with open("andrasi_norbert //otthoni//final caesar//input.txt", "r") as TheInputFile:
    text = TheInputFile.read()
#File beolvasás.
print(text)

while True:
    shift = int(input("Adja meg az eltolás értékét és nyomjon ENTER-t: "))
    try:
        shift = int(shift)
        break
    except:
        print("Számértéket adjon meg")
#Az eltolás értékének ellenőrzése.
encoded_text = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            idx = letters.index(ch)
            encoded_chr = (idx + shift) % len(letters)
            encoded_text += letters[encoded_chr]
        elif ch.islower:
            idx = lowerletters.index(ch)
            encoded_chr = (idx + shift) % len(lowerletters)
            encoded_text += lowerletters[encoded_chr]
    else:
        encoded_text += ch
#A Caesar kód pythonban.
with open("andrasi_norbert //otthoni//final caesar//input.txt", "w") as TheOutputFile:
    TheOutputFile.write(encoded_text)
#Visszaírás a fileba.