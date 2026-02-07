from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            static_url_path='', 
            static_folder='.',
            template_folder='.')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/detail.html')
def detail():
    return render_template('detail.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("Server Silsilah Keluarga Berhasil Dijalankan!")
    print("Akses web di: http://127.0.0.1:5000")
    print("--------------------------------------------------")
    app.run(debug=True, port=5000)