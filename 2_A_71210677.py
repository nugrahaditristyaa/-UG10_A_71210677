#Kalkulator Advance Sederhana

print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

#Mengambil input
menu = int(input("Masukan menu yang anda pilih: "))
if menu == 1:
    b1 = float(input("Masukan bilangan yang ingin dibagi: "))
    b2 = float(input("Masukan bilangan pembagi: "))
    b3 = b1%b2
    print("Sisa hasil bagi ",str(b1)," dibagi dengan ",str(b2)," adalah ",str(b3))
elif menu == 2:
    b4 = float(input("Masukan bilangan yang ingin dibagi: "))
    b5 = float(input("Masukan bilangan pembagi: "))
    b6 = b4//b5
    print("Hasil Pembagian",str(b4),"dibagi dengan",str(b5),"dibulatkan kebawah adalah",str(b6))
elif menu == 3:
    b7 = float(input("Masukan bilangan yang ingin dicari akar kubiknya: "))
    b8 = (b7**(1/3))
    print("Akar kubik dari",str(b7),"adalah",str(b8))
else:
    print("Menu yang anda pilih tidak tersedia")
    
    
    
                
    



