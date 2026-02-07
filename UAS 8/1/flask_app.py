from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/produk")
def produk():
	return render_template("produk.html")

if __name__ == "__main__":
	app.run(debug=True)