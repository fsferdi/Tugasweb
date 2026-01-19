from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

CV_FOLDER = os.path.join(os.getcwd(), 'files')

@app.route("/")
def beranda():
    return render_template("beranda.html")

@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

@app.route("/pendidikan")
def pendidikan():
    return render_template("pendidikan.html")

@app.route("/pengalaman")
def pengalaman():
    return render_template("pengalaman.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

@app.route("/download/pdf")
def download_pdf():
    return send_from_directory(CV_FOLDER, "CV.pdf", as_attachment=True)

@app.route("/download/docx")
def download_docx():
    return send_from_directory(CV_FOLDER, "CV.docx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)