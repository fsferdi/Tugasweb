from antrian import *

while True:
	bersihkan_layar()
	menu()
	pilihan = input_pilihan()
	
	if pilihan == "1":
		tambah_antrian()
	elif pilihan == "2":
		panggil_antrian()
	elif pilihan == "3":
		lihat_antrian()
	elif pilihan == "4":
		print("\nProgram selesai | Terima kasih!")
		break
	else:
		print("Pilihan tidak valid")
		
	input()
	continue