from flask import Flask, render_template, request, redirect, url_for
from core.constants import biodata
from core.services import tambah_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        tempat = request.form.get("tempat")
        tanggal = request.form.get("tanggal")
        jenis = request.form.get("jenis")
        hobi = request.form.getlist("hobi")

        tambah_data(nama, tempat, tanggal, jenis, hobi)

        return redirect(url_for("index"))

    return render_template("biodata.html", biodata=biodata)

if __name__ == "__main__":
    app.run(debug=True)