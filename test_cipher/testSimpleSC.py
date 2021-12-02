import random, sys

def encrypt(message, key):
    translated = ''
    charsA = LETTERS
    charsB = key   
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated
    
def decrypt(message, key):
    translated = ''
    charsB = LETTERS
    charsA = key   
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated
    
def getRandomKey():
    randomList = list(LETTERS)
    random.shuffle(randomList)
    return ''.join(randomList)
    
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'defend the east wall of the castle'
key = ''
key = input("Enter 26 ALPHA key (blank for random key): ")
if key == '':
    key = getRandomKey()
    
translated = encrypt(message, key)
print('Using key: %s' % (key))
print('Cipher: ' + translated)
print('Plain: ' + decrypt(translated,key))