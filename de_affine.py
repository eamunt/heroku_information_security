def decryptChar(char):
    K1, K2, KI = KEY
    if (char.isupper()):
        return chr(KI * ((ord(char)-65) - K2) % 26 + 65)
    elif char.islower():
        return chr(KI * ((ord(char)-97) - K2) % 26 + 97)
    else:
        return char
    
def decryptAffine(string, k1, k2):
    string = str(string)
    k1 = int(k1)
    k2 = int(k2)
    global KEY
    KEY = (k1, k2, mod_inverse(k1,26) )        

    str1 = ''
    for char in string:
        str1 += decryptChar(char)
    return str1    

def mod_inverse(x,m): #tìm nghịch đảo của 7 sẽ là 15
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1: #không tìm được nghịch đảo
            return "Null"
        else:
            continue
