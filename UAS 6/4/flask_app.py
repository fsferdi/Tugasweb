from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def lulus():
	nama = ""
	hasil = ""
	
	if request.method == "POST":
		nama = request.form["nama"]
		nilai = int(request.form["nilai"])
		
		if nilai >= 50:
			hasil = "Lulus"
		else:
			hasil = "Tidak Lulus"
			
	return render_template("main.html", nama=nama, hasil=hasil)
	
if __name__ == "__main__":
	app.run(debug=True)