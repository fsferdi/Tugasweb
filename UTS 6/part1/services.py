def angka_ke_label(angka):
	if angka >= 85:
		return "A"
	elif angka >= 80:
		return "A-"
	elif angka >= 75:
		return "B+"
	elif angka >= 70:
		return "B"
	elif angka >= 65:
		return "B-"
	elif angka >= 60:
		return "C+"
	elif angka >= 55:
		return "C"
	elif angka >= 45:
		return "D"
	else:
		return "E"
	
def label_ke_bobot(label):
	label = label.upper()
	if label == "A":
		return 4
	elif label == "A-":
		return 3.75
	elif label == "B+":
		return 3.5
	elif label == "B":
		return 3
	elif label == "B-":
		return 2.75
	elif label == "C+":
		return 2.5
	elif label == "C":
		return 2
	elif label == "D":
		return 1
	else:
		return 0
	
def sks_yang_diambil(list_sks):
	hasil = sum(list_sks)
	return hasil
	
def total_nilai(list_nilai):
	hasil = sum(list_nilai)
	return hasil
	
def hitung_total_nilai(daftar_sks, daftar_nilai):
	daftar_label = [angka_ke_label(angka) for angka in daftar_nilai]
	daftar_bobot = [label_ke_bobot(label) for label in daftar_label]
	
	daftar_n = []
	for i in range(0, len(daftar_sks), 1):
		temp = daftar_sks[i] * daftar_bobot[i]
		daftar_n.append(temp)
	
	return sum(daftar_n)
	
def ips(total_nilai, total_sks):
	if total_sks == 0:
		return 0
	return total_nilai / total_sks