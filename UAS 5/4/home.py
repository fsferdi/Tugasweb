def clear():
	import os
	os.system("clear")

while True:
	clear()
	nama = input("nama: ").lower()
	
	print(nama.capitalize() if nama in ["budi", "andi"] else "anda bukan budi atau andi")
	
	input()
	continue