from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
	msg = None
	
	if request.method == "POST":
		if request.form["username"] == "admin" and request.form["password"] == "admin":
			msg = "berhasil login"
		else:
			msg = "gagal login"
			
	return render_template("login.html", msg=msg)
	
if __name__ == "__main__":
	app.run(debug=True)