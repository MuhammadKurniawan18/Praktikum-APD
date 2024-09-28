loop = 0
while loop < 3:

    username = input("Masukan username anda : ")
    password = int(input("Masukan password anda : "))
    if username == "Muhammad Kurniawan" and password == 91:
        Lanjut = input("Mau lanjut apa ga nihh?? : ")
        if Lanjut == "Ga lanjut ah":
            print("Program di hentikan")
        else:
            print("Nice, lanjut ke tahap selanjutnya")
        hari = input("Masukan hari : ")
        uang = int(input("Uang yang anda miliki : "))
        if hari == "Senin" or hari == "Selasa" or hari == "Rabu" or hari == "Kamis":
            if uang >= 40000:
                print(f"Ciee uangnya cukup untuk beli tikett di hari {hari} kiwkiwww")
                break
            else:
                print("Hadehhh, sudah tau ga cukup masih nanya")
                break
        elif hari == "Jumat":
            if uang >= 45000:
                print("Ciee uangnya cukup untuk beli tikett di hari jumat kiwkiwwww")
                break
            else:
                print("Hadehhh, sudah tau ga cukup masih nanya")
                break
        elif hari == "Sabtu":
            if uang >= 50000:
                print("Ciee uangnya cukup untuk beli tikett di hari sabtu kiwkiwwww")
                break
            else:
                print("Hadehhh, sudah tau ga cukup masih nanya")
                break
        elif hari == "Minggu":
            if uang >= 55000:
                print("Ciee uangnya cukup untuk beli tikett di hari minggu kiwkiwwww")
                break
            else:
                print("Hadehhh, sudah tau ga cukup masih nanya")
                break
        else:
            print("Hari apasih yg anda masukan gajelas bgttt ??!!")
            break
    else:
        print("Username atau Password yang anda masukan salah. Mau lanjut apa nda nih??")
        Lanjut = input()
        if Lanjut == "Iya":
            print("Program di hentikan")
        else:
            loop = loop + 1
            print(f"Anda sudah mencoba sebanyak {loop} kali")