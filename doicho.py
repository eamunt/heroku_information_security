#hoán vị các ký tự của bản rõ theo chu kỳ cố định d

def split_len(seq, length): # tách từng cụm có dộ dài length
    return [ seq[i:i + length] for i in range(0, len(seq),length) ] 

def encryptDoicho(text, key):
    text = str(text)
    key = str(key)
    text = text.replace(" ","") #del space
    order = {
        int(val): num for num, val in enumerate(key) #[(0,'1'),(1,'2')]
    }
    e_text = ""
    for index in sorted(order.keys()):
        #sorted: sắp xếp các ký tự lại
        #print(order.keys())
        #print(index)
        for part in split_len(text, len(key)):
            print(part) #tách từng cụm 3 ký tự
            try:
                e_text += part[order[index]]# lấy vị trí order[index] trong từng phần
                print(order[index]) # index=2 => order(2)=4
                print(e_text)
            except IndexError: # hết part rồi.
                continue
    return e_text

def decryptDoicho(e_text, key):
    text = str(e_text)
    key = str(key)
    e_text = e_text.replace(" ","")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    d_text = ""
    n = int(len(e_text)/len(key)) # n=6/3=2
    for index in sorted(order.keys()):
        for part in split_len(e_text, n):
            try:
                d_text += part[order[index]]
            except IndexError:
                continue
    return d_text