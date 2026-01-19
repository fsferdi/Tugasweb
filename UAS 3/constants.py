from datetime import date

HARGA_MOTOR = 5000
HARGA_MOBIL = 10000

parkir = {}

analisis = {
    "motor": 7,
    "mobil": 4
}

def rupiah(n):
    return f"Rp {n:,}".replace(",", ".")

def kendaraan_masuk(plat, jenis, merk):
    if not plat or not merk:
        return "Data belum lengkap"
    if plat in parkir:
        return "Plat sudah terdaftar"
    parkir[plat] = {"jenis": jenis, "merk": merk}
    return "Kendaraan berhasil masuk"

def kendaraan_keluar(plat):
    if plat not in parkir:
        return None

    data = parkir.pop(plat)
    if data["jenis"] == "Motor":
        analisis["motor"] += 1
        biaya = HARGA_MOTOR
    else:
        analisis["mobil"] += 1
        biaya = HARGA_MOBIL

    return data, rupiah(biaya)

def get_analisis():
    motor = analisis["motor"]
    mobil = analisis["mobil"]

    harian = (motor * HARGA_MOTOR) + (mobil * HARGA_MOBIL)

    return {
        "tarif_motor": rupiah(HARGA_MOTOR),
        "tarif_mobil": rupiah(HARGA_MOBIL),
        "motor": motor,
        "mobil": mobil,

        "harian": rupiah(harian),
        "mingguan": rupiah(harian * 7),
        "bulanan": rupiah(harian * 31),
        "tahunan": rupiah(harian * 365),

        "tgl_harian": "17-01-2026",
        "tgl_mingguan": "18-012026",
        "tgl_bulanan": "01-2026",
        "tgl_tahunan": "2026"
    }