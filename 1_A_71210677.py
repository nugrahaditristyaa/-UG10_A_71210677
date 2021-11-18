#Kalkulator Replika Penghitung Nilai PrakTekKom

#mengambil input
a1 = float(input("Masukan nilai rata-rata UG anda: "))
b1 = float(input("Masukan nilai TTS anda: "))
c1 = float(input("Masukan nilai TAS anda: "))
print("=========================")
h = ((a1*0.7)+(b1*0.15)+(c1*0.15))
print("Nilai anda: " + str(h))

if h >= 85:
    print("Nilai huruf anda: A")
elif h >= 80:
    print("Nilai huruf anda: A-")
elif h >= 75:
    print("Nilai huruf anda: B+")
elif h >= 70:
    print("Nilai huruf anda: B")
elif h >= 65:
    print("Nilai huruf anda: B-")
elif h >= 60:
    print("Nilai huruf anda: C+")
elif h >= 55:
    print("Nilai huruf anda: C")
elif h >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")



