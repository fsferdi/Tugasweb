import os

def judul(teks):
    print(f"\n+-----{teks}-----+")

def menu():
    judul("Menu utama")
    print("1. Biodata")
    print("2. SKS")
    print("3. Input nilai")
    print("4. Lihat nilai")
    print("5. Lihat IP")
    print("6. Keluar")

def input_pilihan():
    return input("Pilihan : ")

def bersihkan_layar():
	import os
	os.system("clear")

def pause():
    input("\nTekan ENTER untuk lanjut...")