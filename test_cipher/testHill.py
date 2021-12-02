import numpy as np

def encryptHill(msg, key):
    msg = msg.replace(" ", "") #Thay thế khoảng trắng
    key = key.replace(" ","")
    K = create_matrix_of_integers_from_string(key) # Tạo ma trận khóa
    len_check = len(msg) % 2 == 0
    if not len_check: # Nếu chiều dài lẻ thì thêm 0 vào cuối
        msg += "0"
    P = create_matrix_of_integers_from_string(msg) #Tách plaintext
    msg_len = int(len(msg) / 2) # Số cột ma trận
    encrypted_msg = ""
    for i in range(msg_len): #Mã hóa P*K 
        row_0 = P[0][i] * K[0][0] + P[1][i] * K[0][1] # Nhân hàng 0 của khóa với cột i của P
        integer = int(row_0 % 26 + 65) # mod 26
        encrypted_msg += chr(integer) # Chuyển thành kí tự
        row_1 = P[0][i] * K[1][0] + P[1][i] * K[1][1] # Nhân hàng 1 của khóa với cột i của P
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def decryptHill(encrypted_msg, key):
    key = key.replace(" ","")
    K = create_matrix_of_integers_from_string(key) # Tạo ma trận khóa
    #Tính định thức
    determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    determinant = determinant % 26
    #Tính nghịch đảo của định thức
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    #Tính ma trận nghịch đảo của khóa K
    K_inverse = K
    K_inverse[0][0], K_inverse[1][1] = K_inverse[1, 1], K_inverse[0, 0]
    K[0][1] *= -1
    K[1][0] *= -1
    for row in range(2):
        for column in range(2):
            K_inverse[row][column] *= multiplicative_inverse
            K_inverse[row][column] = K_inverse[row][column] % 26
    #Tach cipher text
    C = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2) # Số cột ma trận
    decrypted_msg = ""
    for i in range(msg_len): #Giai ma C*K^-1
        column_0 = C[0][i] * K_inverse[0][0] + C[1][i] * K_inverse[0][1] # Nhân hàng 0 của khóa với cột i của P
        integer = int(column_0 % 26 + 65) # mod 26
        decrypted_msg += chr(integer) # Chuyển thành kí tự
        column_1 = C[0][i] * K_inverse[1][0] + C[1][i] * K_inverse[1][1] # Nhân hàng 1 của khóa với cột i của P
        integer = int(column_1 % 26 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0": # Bỏ kí tự 0 ở cuối
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def find_multiplicative_inverse(determinant): #Tìm nghịch đảo của định thức
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1: # Nếu determinant * i = 1 (mod 26) => i là nghịch đảo
            multiplicative_inverse = i
            break
    return multiplicative_inverse

def create_matrix_of_integers_from_string(string): #Tạo ma trận khóa
    integers = [chr_to_int(c) for c in string] # Tạo list chứa các số nguyên tương ứng với các kí tự trong chuỗi
    length = len(integers) # Số kí tự
    M = np.zeros((2, int(length / 2)), dtype=np.int32) # Tạo ma trận zero gồm 2 hàng, (số kí tự / 2) cột
    iterator = 0
    # Tạo ma trận từ các số nguyên trong list
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char): # Chuyển kí tự thành số nguyên 0 - 25
    char = char.upper()
    integer = ord(char) - 65
    return integer

