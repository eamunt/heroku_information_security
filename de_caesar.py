def decryptCaesar(e_text, k):
    e_text = str(e_text)
    k = int(k)
    e_text = e_text.replace(" ","")
    d_text = ""
    for i in range(len(e_text)):
        char = e_text[i]
        if char.isupper():
            d_text += chr((ord(char) -k - 65) % 26 + 65)
        elif (char.islower()):
            d_text += chr((ord(char) -k - 97) % 26 + 97) 
        else:
            d_text += char
    return d_text