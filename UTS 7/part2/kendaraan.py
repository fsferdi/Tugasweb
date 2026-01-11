kendaraan =[]

def menu():
	print("1. Kendaraan Masuk")
	print("2. Kendaraan Keluar")
	print("3. Lihat Parkir")
	print("4. Keluar")
	
def input_pilihan():
	pilihan = input("Pilihan : ")
	return pilihan
	
def kendaraan_masuk():
	plat = input("Plat : ")
	jenis = input("Jenis : ")
	merk = input("Merk : ")
	kendaraan.append([plat, jenis, merk])
	print(f"Berhasil menambahkan kendaraan")
	
def kendaraan_keluar():
	if len(kendaraan) == 0:
		print("Parkiran kosong")
	else:
		plat_cari = input("Plat Kendaraan : ")
		for k in kendaraan:
			if k[0] == plat_cari:
		           	print(f"{k[0]} {k[1]} {k[2]}")
		           	kendaraan.remove(k)
		           	return
		print("Kendaraan tidak ditemukan")
		           	 	 
def lihat_parkir():
	if len(kendaraan) == 0:
		print("Parkiran kosong")
	else:
		print("Daftar Parkir")
		for i, item in enumerate(kendaraan, start=1):
			print(f"{i}. {item[0]}")
			
def bersihkan_layar():
	import os
	os.system("clear")