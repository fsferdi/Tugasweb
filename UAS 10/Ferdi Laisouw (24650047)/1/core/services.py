from core.constants import biodata

def tambah_data(nama, tempat, tanggal, jenis):
    biodata.append({
        "nama": nama,
        "tempat": tempat,
        "tanggal": tanggal,
        "jenis": jenis
    })