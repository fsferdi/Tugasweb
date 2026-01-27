from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
USERNAME = "admin"
PASSWORD = "admin"

@app.route("/", methods=["GET", "POST"])
def login():
	pesan = ""
	
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		
		if username == USERNAME and password == PASSWORD:
			return redirect(url_for("dashboard", user=username))
		else:
			pesan = "Gagal Login"
			
	return render_template("login.html", pesan=pesan)
	
@app.route("/dashboard")
def dashboard():
	user = request.args.get("user")
	return render_template("dashboard.html", user=user)
	
if __name__ == "__main__":
	app.run(debug=True)