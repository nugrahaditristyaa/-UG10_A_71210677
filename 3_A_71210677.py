#Mendatar atau Menurun?

#Mengambil input
a1 = input("Mendatar/Menurun?: ")
if a1 == "Mendatar":
    a2 = int(input("Masukan kolom:"))
    print("#"*a2)
elif a1 == "Menurun":
    a3 = int(input("Masukan baris: "))
    print("*\n"*a3)
else:
    print("Pola tidak dikenali")

