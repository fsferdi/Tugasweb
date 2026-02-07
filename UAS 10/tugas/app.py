from flask import Flask, render_template, request
from core.constants import daftar_produk
from core.services import tambah_produk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def produk():
    