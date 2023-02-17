#hello
#dec to bin
def dec2bin(num):
    res = bin(num).replace("0b", "")
    #print(bin(65)) 0b1000001
    if(len(res)%4 != 0): 
        div = len(res) / 4 
        div = int(div) ##1
        counter =(4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


#dec to hex
def bin2hex(s):
    mp = {"0000" : '0',
        "0001" : '1',
        "0010" : '2',
        "0011" : '3',
        "0100" : '4',
        "0101" : '5',
        "0110" : '6',
        "0111" : '7',
        "1000" : '8',
        "1001" : '9',
        "1010" : 'A',
        "1011" : 'B',
        "1100" : 'C',
        "1101" : 'D',
        "1110" : 'E',
        "1111" : 'F' }
    hex = ""
    for i in range(0,len(s),4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex

def dec2bin_str(text):
    biText = ''
    for i in range(len(text)):
        char = text[i]
        biText += dec2bin(ord(char)) # lấy từng ký tự của text đưa về kiểu bin
    return biText

#hex to bin
def hex2bin(s):
    mp = {'0' : "0000",
        '1' : "0001",
        '2' : "0010",
        '3' : "0011",
        '4' : "0100",
        '5' : "0101",
        '6' : "0110",
        '7' : "0111",
        '8' : "1000",
        '9' : "1001",
        'A' : "1010",
        'B' : "1011",
        'C' : "1100",
        'D' : "1101",
        'E' : "1110",
        'F' : "1111" }
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

#bin to dec
def bin2dec(binary):
    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

#hex to text
def hex2text(h):
    ascii_string = ''
    x = 0
    y = 2
    l = len(h)
    while y <= l:
        ascii_string += chr(int(h[x:y], 16))
        x += 2
        y += 2
    return ascii_string

def encryptXor(text, k):
    text = str(text)
    k = str(k)
    bi_text = ''
    en_text = ''
    #2.
    bi_text = dec2bin_str(text)
    #3.
    bi_key = dec2bin_str(k)

    #4.
    for h in range(len(bi_text)):
        x1 = int(bi_text[h]) # get 1 bit, str2int to XOR 
        if h < len(bi_key): 
            x2 =int(bi_key[h])
        else: 
            x2 = int(bi_key[h%len(bi_key)]) # nếu chiều dài của bi_text lớn hơn thì lấy phần dư cho chiều dài của bi_key
        xo_r = x1^x2 # phép xor từng ký tự
        en_text += str(xo_r) # trả về kiểu str.
    
    hhh = bin2hex(en_text)
    return hhh

def decryptXor(e_text, k):
    e_text = str(e_text)
    k = str(k)
    de_text = ''
    #hex2bin
    bi_text = hex2bin(e_text)
    #dec2bin
    bi_key = dec2bin_str(k)
    dem = 0
    for h in range(len(bi_text)):
        x1 = int(bi_text[h]) # get 1 bit, str2int to XOR 
        if h < len(bi_key): 
            x2 =int(bi_key[h])
        else: 
            x2 = int(bi_key[h%len(bi_key)]) # nếu chiều dài của bi_text lớn hơn thì lấy phần dư cho chiều dài của bi_key
        xo_r = x1^x2 # phép xor từng ký tự
        de_text += str(xo_r) # trả về kiểu str.
        
    de_text = bin2hex(de_text)
    de_text = hex2text(de_text)
    return de_text
