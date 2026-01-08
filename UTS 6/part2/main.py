from cli import *
from services import *

while True:
    bersihkan_layar()
    menu()
    pilihan = input_pilihan()

    if pilihan == "1":
        judul("Biodata")
        input_biodata()
        lihat_biodata()
        pause()

    elif pilihan == "2":
        judul("SKS")
        input_sks()
        lihat_sks()
        pause()

    elif pilihan == "3":
        judul("Input Nilai")
        input_nilai()
        pause()

    elif pilihan == "4":
        judul("Nilai")
        lihat_nilai()
        pause()

    elif pilihan == "5":
        judul("IP")
        hitung_ip()
        pause()

    elif pilihan == "6":
        print("\nProgram selesai | Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
        pause()