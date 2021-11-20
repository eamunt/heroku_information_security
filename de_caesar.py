def decryptCaesar(e_text, k):
    text = str(e_text)
    k = int(k)
    e_text = e_text.replace(" ","")
    d_text = ""
    for i in range(len(e_text)):
        char = e_text[i]
        if char.isupper():
            d_text += chr((ord(char) -k - 65) % 26 + 65)
        else:
            d_text += chr((ord(char) +k - 97) % 26 + 97)
    return d_text