from flask import Flask, render_template, request, redirect, session, abort
import json, uuid, os
from datetime import datetime, timedelta
import qrcode

app = Flask(__name__)
app.secret_key = "secret-key"
DATA_FILE = "data.json"

# ---------- UTIL ----------
def load():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_pertemuan(pid):
    data = load()
    for p in data["pertemuan"]:
        if p["id"] == pid:
            return p
    return None

def login_required(role):
    def wrap(fn):
        def inner(*args, **kwargs):
            if "role" not in session:
                return redirect("/")
            if session["role"] != role:
                abort(403)
            return fn(*args, **kwargs)
        inner.__name__ = fn.__name__
        return inner
    return wrap

def generate_qr(pid, mahasiswa_id):
    token = f"{pid}|{mahasiswa_id}|{uuid.uuid4()}"
    img = qrcode.make(token)
    path = f"static/qr/{pid}_{mahasiswa_id}.png"
    img.save(path)
    return path

# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pw = request.form.get("pw")
        data = load()

        # ADMIN
        if user == data["admin"]["username"] and pw == data["admin"]["password"]:
            session["role"] = "admin"
            session["nama"] = "Admin"
            return redirect("/admin/dashboard")

        # DOSEN
        for d in data["dosen"]:
            if user == d["username"] and pw == d["password"]:
                session["role"] = "dosen"
                session["nama"] = d["nama"]
                return redirect("/dosen/dashboard")

        # MAHASISWA
        for m in data["mahasiswa"]:
            if user == m["username"] and pw == m["password"]:
                session["role"] = "mahasiswa"
                session["nama"] = m["nama"]
                session["id"] = m["username"]
                return redirect("/mahasiswa/dashboard")

        return "Login gagal"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------- ADMIN ----------
@app.route("/admin/dashboard")
@login_required("admin")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/buat-akun", methods=["GET", "POST"])
@login_required("admin")
def buat_akun():
    data = load()
    if request.method == "POST":
        role = request.form["role"]
        data[role].append({
            "nama": request.form["username"],
            "username": request.form["username"],
            "password": request.form["password"]
        })
        save(data)
        return redirect("/admin/dashboard")
    return render_template("admin/buat_akun.html")

# ---------- DOSEN ----------
@app.route("/dosen/dashboard")
@login_required("dosen")
def dosen_dashboard():
    return render_template("dosen/dashboard.html", nama=session["nama"])

@app.route("/dosen/pertemuan", methods=["GET", "POST"])
@login_required("dosen")
def dosen_pertemuan():
    data = load()
    if request.method == "POST":
        data["pertemuan"].append({
            "id": str(uuid.uuid4()),
            "nama": request.form["nama"],
            "tanggal": request.form["tanggal"],
            "masuk": request.form["masuk"],
            "keluar": request.form["keluar"],
            "dibuat": datetime.now().isoformat(),
            "presensi": []
        })
        save(data)
    return render_template("dosen/pertemuan.html", data=data["pertemuan"])

@app.route("/dosen/pertemuan/<pid>")
@login_required("dosen")
def dosen_detail(pid):
    return render_template("dosen/detail.html", p=get_pertemuan(pid))

@app.route("/dosen/scan/<pid>", methods=["POST"])
@login_required("dosen")
def scan(pid):
    token = request.form.get("token")
    if not token:
        return "Token kosong", 400

    data = load()
    p = get_pertemuan(pid)

    try:
        pid_qr, mahasiswa_id, _ = token.split("|")
    except:
        return "QR tidak valid", 400

    if pid_qr != pid:
        return "QR salah pertemuan", 400

    mulai = datetime.strptime(
        p["tanggal"] + " " + p["masuk"],
        "%Y-%m-%d %H:%M"
    )

    if datetime.now() > mulai + timedelta(minutes=15):
        return "QR kadaluarsa", 400

    if mahasiswa_id not in p["presensi"]:
        p["presensi"].append(mahasiswa_id)
        save(data)

    return "Presensi berhasil"

# ---------- MAHASISWA ----------
@app.route("/mahasiswa/dashboard")
@login_required("mahasiswa")
def mhs_dashboard():
    return render_template("mahasiswa/dashboard.html", nama=session["nama"])

@app.route("/mahasiswa/pertemuan")
@login_required("mahasiswa")
def mhs_pertemuan():
    return render_template("mahasiswa/pertemuan.html", data=load()["pertemuan"])

@app.route("/mahasiswa/pertemuan/<pid>")
@login_required("mahasiswa")
def mhs_detail(pid):
    return render_template(
        "mahasiswa/detail.html",
        p=get_pertemuan(pid),
        qr=generate_qr(pid, session["id"])
    )

# ---------- RUN ----------
if __name__ == "__main__":
    os.makedirs("static/qr", exist_ok=True)
    app.run(debug=True)