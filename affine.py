

def mod_inverse(x,m): #tìm nghịch đảo của 7 sẽ là 15
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1: #không tìm được nghịch đảo
            return "Null"
        else:
            continue    

def encryptChar(char):
    K1, K2, kI = KEY
    if (char.isupper()):
        return chr((K1 * (ord(char)-65) + K2) % 26 + 65)
    elif char.islower():
        return chr((K1 * (ord(char)-97) + K2) % 26 + 97)
    elif char == ' ':
        return ''
    else:
        return char

def encryptAffine(string, k1, k2):
    string = str(string)
    k1 = int(k1)
    k2 = int(k2)
    global KEY
    KEY = (k1, k2, mod_inverse(k1,26) )

    str1 = ''
    for char in string:
        str1 += encryptChar(char)
    return str1