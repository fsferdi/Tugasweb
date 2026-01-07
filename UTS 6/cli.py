from services import *

def judul(teks):
	print(f"+---{teks}---+")

def menu():
	print("1. Konversi nilai ke label")
	print("2. Konversi label ke bobot")
	print("3. Hitung total SKS yang diambil")
	print("4. Hitung total nilai")
	print("5. Hitung IPS")
	print("6. Exit")
	
def input_pilihan():
	pilihan = input("Pilihan : ")
	return pilihan
	
def bersihkan_layar():
	import os
	os.system("clear")
	
def form_input_jumlah_mata_kuliah():
	n = input("Jumlah Mata kulaih : ")
	return int(n)
	
def form_input_sks(jumlah_mata_kuliah):
	list_sks = []
	for i in range(0,jumlah_mata_kuliah, 1):
		temp = input(f"SKS {i+1}: ")
		list_sks.append(int(temp))
		
	return list_sks
	
def form_input_nilai(jumlah_mata_kuliah):
	list_nilai = []
	for i in range(0,jumlah_mata_kuliah, 1):
		temp = input(f"SKS {i+1}: ")
		list_nilai.append(int(temp))
		
	return list_nilai
	
def nilai_x_sks(daftar_nilai, daftar_sks):
	hasil = []
	for i in range(0, len(daftar_nilai), 1):
		temp = daftar_nilai[i] * daftar_sks[i]
		hasil.append(temp)
	
	return hasil
		