from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from flask import abort

app = Flask(__name__)
app.secret_key = "secret123"

DATA_FILE = "accounts.json"

def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_accounts(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

accounts = load_accounts()

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    accounts = load_accounts()
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = next(
            (a for a in accounts if a["username"] == username),
            None
        )
        
        if not user:
        	error = "Username tidak terdaftar"
        elif user["password"] != password:
        	error = "Password salah"
        else:
            session["username"] = user["username"]
            session["role"] = user["role"]

            if user["role"] == "Admin":
                return redirect("/dashboard/admin")
            elif user["role"] == "Dosen":
                return redirect("/dashboard/dosen")
            elif user["role"] == "Mahasiswa":
                return redirect("/dashboard/mahasiswa")

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    accounts = load_accounts()

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        role = request.form["role"]

        if any(a["username"] == username for a in accounts):
            error = "Nama sudah terdaftar"
        else:
            accounts.append({
                "username": username,
                "password": password,
                "role": role
            })
            save_accounts(accounts)
            return redirect("/register")

    return render_template("register.html", accounts=accounts, error=error)

@app.route("/delete/<username>")
def delete(username):
    accounts = load_accounts()
    accounts = [a for a in accounts if a["username"] != username]
    save_accounts(accounts)
    return redirect("/register")

@app.route("/dashboard/admin")
def admin():
    if session.get("role") != "Admin":
        abort(403)
    return render_template("dashboard.html", username=session.get("username"), role="Admin")

@app.route("/dashboard/dosen")
def dosen():
    if session.get("role") != "Dosen":
        abort(403)
    return render_template("dashboard.html", username=session.get("username"), role="Dosen")

@app.route("/dashboard/mahasiswa")
def mahasiswa():
    if session.get("role") != "Mahasiswa":
        abort(403)
    return render_template("dashboard.html", username=session.get("username"), role="Mahasiswa")
    
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)