from flask import Flask, render_template, request, redirect, session, abort, flash
import json, uuid, base64
from datetime import datetime, timedelta
import qrcode
from io import BytesIO

app = Flask(__name__)
app.secret_key = "secret-key"

DATA_FILE = "data/accounts.json"

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
    
def generate_qr_base64(pid, mahasiswa_induk):
    token = f"{pid}|{mahasiswa_induk}|{uuid.uuid4()}"
    img = qrcode.make(token)
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return base64.b64encode(buffer.getvalue()).decode()
    
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pw = request.form.get("pw")
        data = load()
        
        if user == data["admin"]["username"] and pw == data["admin"]["password"]:
            session["role"] = "admin"
            session["nama"] = "Admin"
            return redirect("/admin/dashboard")
            
        for d in data["dosen"]:
            if user == d["username"] and pw == d["password"]:
                session["role"] = "dosen"
                session["nama"] = d["nama"]
                session["induk"] = d["induk"]
                return redirect("/dosen/dashboard")
                
        for m in data["mahasiswa"]:
            if user == m["username"] and pw == m["password"]:
                session["role"] = "mahasiswa"
                session["nama"] = m["nama"]
                session["induk"] = m["induk"]
                return redirect("/mahasiswa/dashboard")
                
        flash("Username atau password salah", "error")
        return redirect("/")
        
    return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    
@app.route("/admin/dashboard", methods=["GET", "POST"])
@login_required("admin")
def admin_dashboard():
    data = load()
    
    if request.method == "POST":
        role = request.form.get("role")
        username = request.form.get("username")
        induk = request.form.get("induk")
        password = request.form.get("password")
        
        if role not in ["dosen", "mahasiswa"]:
            flash("Role tidak valid", "error")
            return redirect("/admin/dashboard")
            
        if not username or not induk or not password:
            flash("Semua data wajib diisi", "error")
            return redirect("/admin/dashboard")
            
        for akun in data[role]:
            if akun["induk"] == induk:
                flash("Nomor induk sudah terdaftar", "error")
                return redirect("/admin/dashboard")
                
            if akun["username"].lower() == username.lower():
                flash("Username sudah digunakan", "error")
                return redirect("/admin/dashboard")
                
            if akun["password"] == password:
                flash("Password sudah digunakan", "error")
                return redirect("/admin/dashboard")
                
        data[role].append({
            "nama": username,
            "username": username,
            "induk": induk,
            "password": password
        })
        
        save(data)
        flash("Akun berhasil dibuat", "success")
        return redirect("/admin/dashboard")
        
    return render_template("admin/dashboard.html", data=data)
    
@app.route("/dosen/dashboard")
@login_required("dosen")
def dosen_dashboard():
    return render_template("dosen/dashboard.html", nama=session["nama"], induk=session["induk"])
    
@app.route("/dosen/pertemuan", methods=["GET", "POST"])
@login_required("dosen")
def dosen_pertemuan():
    data = load()
    
    if request.method == "POST":
        data["pertemuan"].append({"id": str(uuid.uuid4()), "nama": request.form["nama"], "tanggal": request.form["tanggal"], "masuk": request.form["masuk"], "keluar": request.form["keluar"], "dibuat": datetime.now().isoformat(), "presensi": []})
        save(data)
        
    return render_template("dosen/pertemuan.html", data=data["pertemuan"])
    
@app.route("/dosen/pertemuan/hapus")
@login_required("dosen")
def hapus_pertemuan():
    data = load()
    data["pertemuan"] = []
    save(data)
    return redirect("/dosen/pertemuan")
    
@app.route("/dosen/pertemuan/<pid>")
@login_required("dosen")
def dosen_detail(pid):
    data = load()
    p = get_pertemuan(pid)
    
    hadir = [
        {"nama": m["nama"], "induk": m["induk"]}
        for m in data["mahasiswa"]
        if m["induk"] in p["presensi"]
    ]
    
    return render_template("dosen/detail.html", p=p, hadir=hadir)
    
@app.route("/dosen/scan/<pid>", methods=["POST"])
@login_required("dosen")
def scan(pid):
    token = request.form.get("token")
    data = load()
    p = get_pertemuan(pid)
    
    if not token:
        return "Token kosong", 400
        
    try:
        pid_qr, mahasiswa_induk, _ = token.split("|")
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
        
    if mahasiswa_induk not in p["presensi"]:
        p["presensi"].append(mahasiswa_induk)
        save(data)
        
    return redirect(f"/dosen/pertemuan/{pid}")
    
@app.route("/dosen/mahasiswa")
@login_required("dosen")
def dosen_mahasiswa():
    data = load()
    return render_template("dosen/mahasiswa.html", mahasiswa=data["mahasiswa"])
    
@app.route("/mahasiswa/dashboard")
@login_required("mahasiswa")
def mahasiswa_dashboard():
    return render_template("mahasiswa/dashboard.html", nama=session["nama"], induk=session["induk"])
    
@app.route("/mahasiswa/pertemuan")
@login_required("mahasiswa")
def mahasiswa_pertemuan():
    data = load()
    return render_template("mahasiswa/pertemuan.html", data=data["pertemuan"])
    
@app.route("/mahasiswa/pertemuan/<pid>")
@login_required("mahasiswa")
def mahasiswa_detail(pid):
    p = get_pertemuan(pid)
    qr_base64 = generate_qr_base64(pid, session["induk"])
    
    return render_template("mahasiswa/detail.html", p=p, qr=qr_base64)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)