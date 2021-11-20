import caesar # import hema
import de_caesar # import hema
import affine
import de_affine

from flask import Flask, request, render_template, jsonify
app = Flask(__name__, template_folder="temp")

#home
@app.route('/')
def home():
    return render_template('trangchu.html') 

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





#sử dụng app.run() để chạy web flask
if(__name__=='__main__'):
    app.run(debug=True)