antrian = []

def menu():
	print("1. Tambah Antrian")
	print("2. Panggil Antrian")
	print("3. Lihat Antrian")
	print("4. Keluar")
	
def input_pilihan():
	pilihan = input("Pilihan : ")
	return pilihan
	
def tambah_antrian():
	nama = input("Nama : ")
	antrian.append(nama)
	print(f"Antrian '{nama}' berhasil ditambahkan")
	
def panggil_antrian():
	if len(antrian) == 0:
		print("Antrian kosong")
	else:
		panggil = antrian.pop(0)
		print(f"Memanggil {panggil}")
	
def lihat_antrian():
	if len(antrian) == 0:
		print("Antrian kosong")
	else:
		print("Daftar antrian: ")
		for i, item in enumerate(antrian, start=1):
			print(f"{i}. {item}")
			
def bersihkan_layar():
	import os
	os.system("clear")