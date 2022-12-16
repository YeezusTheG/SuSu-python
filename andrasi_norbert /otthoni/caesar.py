with open("text.txt", "r") as inputfile:  #Az elérési útvonalat majd lehet meg kell változtatni
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
        if ch.islower():
            ascii_value = (ascii_value - 97 + shift) % 26 + 97
        else:
            ascii_value = (ascii_value - 65 + shift) % 26 + 65
        cipher_text += chr(ascii_value)
    else:
        cipher_text += ch

with open("text.txt", "w") as outputfile: #Az elérési útvonalat majd lehet meg kell változtatni itt is
    outputfile.write(cipher_text)