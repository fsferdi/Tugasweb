from flask import Flask, render_template, request
import constants

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def masuk():
    pesan = None
    if request.method == "POST":
        pesan = constants.kendaraan_masuk(
            request.form["plat"],
            request.form["jenis"],
            request.form["merk"]
        )
    return render_template("menu.html", page="masuk", pesan=pesan)

@app.route("/keluar", methods=["GET", "POST"])
def keluar():
    hasil = None
    if request.method == "POST":
        hasil = constants.kendaraan_keluar(request.form["plat"])
    return render_template("menu.html", page="keluar", hasil=hasil)

@app.route("/parkir")
def parkir():
    return render_template("menu.html", page="parkir", data=constants.parkir)

@app.route("/analisis")
def analisis():
    return render_template("index.html", data=constants.get_analisis())

if __name__ == "__main__":
    app.run(debug=True)