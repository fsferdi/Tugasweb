daftar_label = ["b", "a", "c", "a", "b"]

def hitung_selain_a(daftar_label):
    hasil = 0
    for label in daftar_label:
        if label != "a":
            hasil += 1
    return hasil

print(hitung_selain_a(daftar_label))