# Inisialisasi data pengguna dan data buah
akun_pengguna = []
data_buah = []
buah = []

while True:
    print("Halo! Selamat Datang di List Pembelian Buah 😊")
    print("Silakan pilih 'Daftar akun' jika belum punya akun, dan jika sudah memiliki akun silahkan 'Login'😊")
    print("――――――――――――――――――――――――")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi😊: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu 😊")
        Username = input("Username: ")
        akuna = False
        for akun in akun_pengguna:
            if akun[0] == Username:  # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi 😁")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (penjual/pengguna): ").lower()
            if role not in ['penjual', 'pengguna']:
                print("Peran tidak valid. Harus 'admin' atau 'pengguna'.")
                continue
            akun_pengguna.append([Username, Password, role, []])  # Simpan username, password, dan data buah (sebagai list kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username} 😁")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akun_pengguna:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("―――Silakan pilih langkah yang kamu mau 😊!―――")
                    if akun[2] == 'penjual': 
                        print("1. Tambah data buah")
                        print("2. Lihat data buah")
                        print("3. Edit data buah")
                        print("4. Hapus data buah")
                    else:
                        print("1. Beli Buah") 
                        print("2. Lihat buah apa saja yang sudah di beli")
                    print("5. Exit")
                    print("―――――――――――――――――――――――――――――")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        if akun[2] == 'penjual':
                            jenis_buah = input("Jenis buah: ")
                            harga_buah = input("Harga buah: ")
                            berat_buah = input("Berat buah (Kg): ")
                            data_buah.append([jenis_buah, harga_buah, berat_buah])  # Menambahkan data buah ke dalam list
                            print("Data buah berhasil ditambahkan!\n")
                        else: 
                            jenis_buah = input("Jenis buah: ")
                            for buah in data_buah:
                                if buah[0] == jenis_buah:
                                    akun[3].append([jenis_buah, buah[1], buah[2]]) #menambahkan buah ke dalam list
                                    print("Buah berhasil dibeli!\n")
                                    break
                            else:
                                print("buah tidak tersedia.\n")

                    elif status == "2":
                        if akun[2] == 'penjual':
                            for buah in data_buah:
                                print(f"Jenis buah: {buah[0]}\nHarga buah: {buah[1]}\nBerat Buah: {buah[2]} Kg\n")
                            if not data_buah:
                                print("Opps, saat ini kamu belum punya data buah, silahkan tambah data buah terlebih dahulu.\n")
                        else:
                            for buah in akun[3]:
                                print(f"Jenis buah: {buah[0]}\nHarga buah: {buah[1]}\nBerat Buah: {buah[2]} Kg\n")
                            if not akun[3]:
                                print("Opps, saat ini kamu belum punya buah, silahkan beli buah terlebih dahulu.\n")

                    elif status == "3":
                        if akun[2] == 'penjual':
                            if not data_buah:
                                print("Tidak ada data buah yang bisa diedit.")
                            else:
                                edit = int(input("Data buah nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(data_buah):
                                    jenis_baru = input("Masukkan jenis yang baru: ")
                                    harga_baru = input("Masukkan harga yang baru: ")
                                    berat_baru = input("Masukkan berat yang baru (Kg): ")
                                    print("Apa kamu yakin ingin mengedit data buah ?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_edit = input("Pilih: ")
                                    if memastikan_edit == "1":
                                        data_buah[edit] = [jenis_baru, harga_baru, berat_baru]  # Mengedit data buah
                                        print("Data buah yang kamu pilih sudah di edit ya!\n")
                                    elif memastikan_edit == "2":
                                        print("Aksi untuk mengedit data buah dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor data buah yang kamu maksud, silahkan input ulang.\n")

                    elif status == "4":
                        if akun[2] == 'penjual':
                            if not data_buah:
                                print("Tidak ada data buah yang bisa dihapus.")
                            else:
                                hapus = int(input("Data buah nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(data_buah):
                                    print(f"Apa kamu yakin ingin menghapus data buah ? ")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del data_buah[hapus]  # Menghapus data buah dari list
                                        print("Data buah yang kamu pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus data buah dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor data buah yang kamu maksud, silahkan input ulang.\n")

                    elif status == "5":
                        print("Aplikasi List Pembelian Buah ditutup.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari aplikasi🧐? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan👌😊!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n 😊")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3 😊")