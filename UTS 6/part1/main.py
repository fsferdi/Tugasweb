from cli import *
from services import *

while True:
	bersihkan_layar()
	menu()
	pilihan = input_pilihan()
	
	if pilihan == "1":
		judul("Konversi nilai ke label")
		angka = input("Masukkan angka : ")
		hasil = angka_ke_label(int(angka))
		print(hasil)
	
	elif pilihan == "2":
		judul("Konversi label ke bobot")
		label = input("Masukkan label : ")
		hasil = label_ke_bobot(str(label))
		print(hasil)
		
	elif pilihan == "3":
		judul("Hitung total SKS yang diambil")
		jumlah_mata_kuliah = input("Jumlah mata kuliah : ")
		jumlah_sks = form_input_sks(int(jumlah_mata_kuliah))
		hasil = sks_yang_diambil(jumlah_sks)
		print(hasil)
		
	elif pilihan == "4":
		judul("SKS")
		jumlah_mata_kuliah = form_input_jumlah_mata_kuliah()
		daftar_sks = form_input_sks(jumlah_mata_kuliah)
		judul("Nilai")
		daftar_nilai = form_input_nilai(jumlah_mata_kuliah)
		hasil = hitung_total_nilai(daftar_sks, daftar_nilai)
		print(hasil)
		
	elif pilihan == "5":
		judul("Hitung IPS")
	
		jumlah_mata_kuliah = form_input_jumlah_mata_kuliah()
	
		judul("SKS")
		daftar_sks = form_input_sks(jumlah_mata_kuliah)
	
		judul("Nilai")
		daftar_nilai = form_input_nilai(jumlah_mata_kuliah)
	
		total_nilai = hitung_total_nilai(daftar_sks, daftar_nilai)
		total_sks = sks_yang_diambil(daftar_sks)
	
		hasil_ips = ips(total_nilai, total_sks)
		print(f"IPS Anda : {hasil_ips:.2f}")
		
	elif pilihan == "6":
		break
		
	input()
	continue
		