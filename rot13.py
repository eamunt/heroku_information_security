n=13
def encryptRot13(text):
    text = str(text)
    text = text.replace(" ","") #del space
    e_text = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()): ## upper
            e_text += chr( (ord(char) - 65 + n)%26 +65) 
        elif (char.islower()): ##lower
            e_text += chr( (ord(char) - 97 + n)%26 +97)
        else:
            e_text += char
    return e_text


def decryptRot13(e_text):
    e_text = str(e_text)
    e_text = e_text.replace(" ","") #del space
    d_text = ""
    for i in range(len(e_text)):
        char = e_text[i]
        if (char.isupper()): ##upper
            d_text += chr( (ord(char) - 65 - n)%26 +65) 
        elif (char.islower()): ##lower
            d_text += chr( (ord(char) - 97 - n)%26 +97)
        else:
            d_text += char
    return d_text
