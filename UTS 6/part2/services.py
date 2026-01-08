from cli import judul

biodata = {}
total_sks = 0
nilai = []

def input_biodata():
    biodata["nama"] = input("Nama  : ")
    biodata["nim"] = input("NIM   : ")
    biodata["prodi"] = input("Prodi : ")
    print("Biodata berhasil disimpan.")

def lihat_biodata():
    if not biodata:
        print("Biodata belum diisi.")
    else:
        judul("Biodata Mahasiswa")
        print("Nama  :", biodata["nama"])
        print("NIM   :", biodata["nim"])
        print("Prodi :", biodata["prodi"])

def input_sks():
    global total_sks
    total_sks = int(input("\nMasukkan total SKS: "))
    print("SKS berhasil disimpan.")

def lihat_sks():
    print("Total SKS:", total_sks)

def input_nilai():
    n = float(input("\nMasukkan nilai (0-100): "))
    nilai.append(n)
    print("Nilai berhasil ditambahkan.")

def lihat_nilai():
    if not nilai:
        print("Belum ada nilai.")
    else:
        print("\nDaftar Nilai:")
        for i, n in enumerate(nilai, start=1):
            print(f"{i}. {n}")

def hitung_ip():
    if not nilai:
        print("Belum ada nilai.")
        return
    ip = (sum(nilai) / len(nilai)) / 25
    print(f"IP Anda: {ip:.2f}")