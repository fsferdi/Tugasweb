from kendaraan import *

while True:
	bersihkan_layar()
	menu()
	pilihan = input_pilihan()
	
	if pilihan == "1":
		kendaraan_masuk()
	elif pilihan == "2":
		kendaraan_keluar()
	elif pilihan == "3":
		lihat_parkir()
	elif pilihan == "4":
		print("\nProgram selesai | Terima kasih!")
		break
	else:
		print("Pilihan tidak valid")
		
	input()
	continue