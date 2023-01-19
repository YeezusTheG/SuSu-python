with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /otthoni/text.txt", "r") as inputfile:  #Az elérési útvonalat majd lehet meg kell változtatni
    text = inputfile.read()
while True:
    shift = int(input("Adja meg az eltolás értékét és nyomjon ENTER-t: "))
    try:
        shift = int(shift)
        break
    except:
        print("Számértéket adjon meg")

cipher_text = ""

for ch in text:
    if ch.isalpha():
        ascii_value = ord(ch)
        if ch in 'áéíóőúüű':
            ascii_value = (ascii_value - 225 + shift) % 8 + 225
        elif ch in 'ÁÉÍÓŐÚÜŰ':
            ascii_value = (ascii_value - 193 + shift) % 8 + 193
        if ch.islower():
            ascii_value = (ascii_value - 97 + shift) % 26 + 97
        elif ch.isupper():
            ascii_value = (ascii_value - 65 + shift) % 26 + 65
        cipher_text += chr(ascii_value)
    else:
        cipher_text += ch

with open("/home/markali/Dokumentumok/GitHub/SuSu-python/andrasi_norbert /otthoni/text.txt", "w") as outputfile: #Az elérési útvonalat majd lehet meg kell változtatni itt is
    outputfile.write(cipher_text)