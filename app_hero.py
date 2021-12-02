import caesar # import hema
import de_caesar # import hema
import affine
import de_affine
import doicho
import xor
import hemanhan
import reverse
import rot13
import vigenere
import hill
import simpleSC

from flask import Flask, request, render_template, jsonify
app = Flask(__name__, template_folder="temp")

#home
@app.route('/')
def home():
    return render_template('trangchu.html') 


#####################################################################################################################
## he ma Caesar
@app.route('/caesar_e',methods=['GET'])
def caesar_e():
    return render_template('caesar.html')

@app.route('/caesar_d',methods=['GET'])
def caesar_d():
    return render_template('de_caesar.html')   

@app.route('/encryptCaesar',methods=['GET'])
def enCaesar():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = caesar.encryptCaesar(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/decryptCaesar',methods=['GET'])
def deCaesar():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = de_caesar.decryptCaesar(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)



#####################################################################################################################
## he ma affine
@app.route('/affine_e',methods=['GET'])
def affine_e():
    return render_template('affine.html')

@app.route('/affine_d',methods=['GET'])
def affine_d():
    return render_template('de_affine.html') 

@app.route('/encryptAffine',methods=['GET'])
def enAffine():
    p = request.args.get('t') # get plaintext
    k1 = request.args.get('key1') # get key
    k2 = request.args.get('key2') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = affine.encryptAffine(p,k1,k2)

    # Render the output in new HTML page
    return render_template('output.html', result=res) 

@app.route('/decryptAffine',methods=['GET'])
def deAffine():
    t = request.args.get('t') # get plaintext
    k1 = request.args.get('key1') # get key
    k2 = request.args.get('key2') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = de_affine.decryptAffine(t,k1,k2)

    # Render the output in new HTML page
    return render_template('output.html', result=res) 


#####################################################################################################################
##he ma doi cho
@app.route('/doicho_e',methods=['GET'])
def doicho_e():
    return render_template('doicho.html')

@app.route('/encryptDoicho',methods=['GET'])
def enDoicho():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = doicho.encryptDoicho(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/doicho_d',methods=['GET'])
def doicho_d():
    return render_template('de_doicho.html')

@app.route('/decryptDoicho',methods=['GET'])
def deDoicho():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = doicho.decryptDoicho(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)


#####################################################################################################################
## he ma XOR
@app.route('/xor_e',methods=['GET'])
def xor_e():
    return render_template('xor.html')

@app.route('/encryptXor',methods=['GET'])
def enXor():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = xor.encryptXor(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/xor_d',methods=['GET'])
def xor_d():
    return render_template('de_xor.html')

@app.route('/decryptXor',methods=['GET'])
def deXor():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = xor.decryptXor(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

#####################################################################################################################
## he ma nhan
@app.route('/hemanhan_e',methods=['GET'])
def hemanhan_e():
    return render_template('hemanhan.html')

@app.route('/encryptHemanhan',methods=['GET'])
def enHemanhan():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = hemanhan.encryptHemanhan(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/hemanhan_d',methods=['GET'])
def hemanhan_d():
    return render_template('de_hemanhan.html')

@app.route('/decryptHemanhan',methods=['GET'])
def deHemanhan():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = hemanhan.decryptHemanhan(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

#####################################################################################################################
## He ma dao nguoc
@app.route('/reverse_e',methods=['GET'])
def reverse_e():
    return render_template('reverse.html')

@app.route('/encryptReverse',methods=['GET'])
def enReverse():
    p = request.args.get('t') # get plaintext
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = reverse.encryptReverse(p)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/reverse_d',methods=['GET'])
def reverse_d():
    return render_template('de_reverse.html')

@app.route('/decryptReverse',methods=['GET'])
def deReverse():
    t = request.args.get('t') 
    res = reverse.decryptReverse(t)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

#####################################################################################################################
## ROT13
@app.route('/rot13_e',methods=['GET'])
def rot13_e():
    return render_template('rot13.html')

@app.route('/encryptRot13',methods=['GET'])
def enRot13():
    p = request.args.get('t') # get plaintext
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = rot13.encryptRot13(p)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/rot13_d',methods=['GET'])
def rot13_d():
    return render_template('de_rot13.html')

@app.route('/decryptRot13',methods=['GET'])
def deRot13():
    t = request.args.get('t') 
    res = rot13.decryptRot13(t)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

#####################################################################################################################
## Vigenere
@app.route('/vigenere_e',methods=['GET'])
def vigenere_e():
    return render_template('vigenere.html')

@app.route('/vigenere_d',methods=['GET'])
def vigenere_d():
    return render_template('de_vigenere.html')   

@app.route('/encryptVigenere',methods=['GET'])
def enVigenre():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = vigenere.encryptVigenere(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/decryptVigenere',methods=['GET'])
def deVigenere():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = vigenere.decryptVigenere(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

#####################################################################################################################
## HILL
'''@app.route('/hill_e',methods=['GET'])
def hill_e():
    return render_template('hill.html')

@app.route('/encryptHill',methods=['GET'])
def enHill():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = hill.encryptHill(p,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)

@app.route('/hill_d',methods=['GET'])
def hill_d():
    return render_template('de_hill.html')

@app.route('/decryptHill',methods=['GET'])
def deHill():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = hill.decryptHill(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)'''

#####################################################################################################################
## SimpleSC
@app.route('/simpleSC_e',methods=['GET'])
def simpleSC_e():
    return render_template('simpleSC.html')

@app.route('/encryptSimpleSC',methods=['GET'])
def enSimpleSC():
    p = request.args.get('t') # get plaintext
    k = request.args.get('key') # get key
    #chuyển dữ liệu qua hàm encrypt của file hema
    res = simpleSC.encryptSimpleSC(p,k)
    key1 = simpleSC.t_key
    # Render the output in new HTML page
    return render_template('output_simpleSC.html', result=res, keyt = key1)

@app.route('/simpleSC_d',methods=['GET'])
def simpleSC_d():
    return render_template('de_simpleSC.html')

@app.route('/decryptSimpleSC',methods=['GET'])
def deSimpleSC():
    t = request.args.get('t') 
    k = request.args.get('key') 
    res = simpleSC.decryptSimpleSC(t,k)

    # Render the output in new HTML page
    return render_template('output.html', result=res)




#sử dụng app.run() để chạy web flask
if(__name__=='__main__'):
    app.run(debug=True)