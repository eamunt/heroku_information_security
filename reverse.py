def encryptReverse (mess):
    mess = str(mess)
    mess = mess.replace(" ","") #xóa khoảng trắng
    i = len(mess) - 1 # lấy ra vị trí ký tự cuối
    translated = '' #khoitao
    while i>=0:
        translated = translated + mess[i]
        i = i - 1
    return translated

def decryptReverse (mess_en):
    mess_en = str(mess_en)
    mess_en = mess_en.replace(" ","")
    i = len(mess_en) - 1
    decrypted = ''
    while i>=0:
        decrypted = decrypted + mess_en[i]
        i = i - 1
    return decrypted
