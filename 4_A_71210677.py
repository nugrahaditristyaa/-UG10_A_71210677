#Skor Pertandingan Sepak Bola

#Mengambil input
artikel = input("Masukan artikel yang ingin dipindai: ")
klub = input("Masukan nama klub favorit anda: ")
skor = input("Masukan skor yang ingin dicari: ")
hklub = klub in artikel
hskor = skor in artikel
if(hklub and hskor):
    print("Hasil pencarian ditemukan")
elif(hklub and not hskor):
    print("Hanya kata",klub,"yang ditemukan pada artikel ini")
elif(not hklub and hskor):
    print("Hanya skor",skor,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",klub,"dan",skor,"tidak ditemukan")
