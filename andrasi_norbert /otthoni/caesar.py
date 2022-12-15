text = "aello, world!"
shift = 72
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

print(cipher_text)