Nama = input("Masukan Nama Anda: ")
Hari = input("Masukan hari yang anda inginkan: ")
Uang = int(input("Masukan uang yang anda miliki: "))

Hargatiket = 0
if Hari == "Senin" or "Selasa" or "Rabu" or "Kamis" :
    if Uang >= 40000:
        print(f"Cie uangnya cukup buat beli tiket di hari {Hari}")
    else:
        print("Udah tau uangnya ga cukup masih nanyaa hedeh")
elif Hari == "Jumat" :
    if Uang >= 45000: 
        print("Cie uangnya cukup buat beli tiket di hari Jumat kiwkiw")
    else:
        print("Udah tau uangnya ga cukup masih nanyaa hedeh")
elif Hari == "Sabtu" : 
    if Uang >= 50000:
        print("Cie uangnya cukup buat beli tiket di hari Sabtu kiwkiw")
    else:
        print("Udah tau uangnya ga cukup masih nanyaa hedeh")
elif Hari == "Minggu" : 
    if Uang >= 55000:
        print("Cie uangnya cukup buat beli tiket di hari Minggu kiwkiw")
    else:
        print("Udah tau uangnya ga cukup masih nanyaa hedeh")
 