
def encryptVigenere(plaintext, key):
    plaintext = str(plaintext)
    key = str(key)
    key = key.replace(" ","")
    key_length = len(key) #
    plaintext = plaintext.replace(" ","")
    key_as_int = [ord(i) for i in key] # 
    plaintext_int = [ord(i) for i in plaintext] #same
    ciphertext = ''
    for i in range(len(plaintext_int)):
        char = plaintext[i]
        if char.isupper():
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value+ord('A'))
        elif char.islower():
            value = (plaintext_int[i]-ord('a') + key_as_int[i % key_length]-ord('a')) % 26 #
            ciphertext += chr(value+ord('a'))
        else:
            ciphertext += char
    return ciphertext

def decryptVigenere(ciphertext, key):
    ciphertext = str(ciphertext)
    key = str(key)
    key = key.replace(" ","")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext = ciphertext.replace(" ","")
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        char = ciphertext[i]
        if char.isupper():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value+ord('A'))
        elif char.islower():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value+ord('a'))
        else:
            plaintext += char
    return plaintext