# Nạp các gói thư viện cần thiết
def encryptCaesar(text, k):
    text = str(text)
    k = int(k)
    text = text.replace(" ","") #del space
    e_text = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()): #isupper
            e_text += chr((ord(char) + k - 65) % 26 + 65) #chr(65) = A -- ord('A')=65
        elif (char.islower()):
            e_text += chr((ord(char) + k - 97) % 26 + 97) #chr(97) = a -- ord('a')=97
        else:
            e_text += char
    return e_text