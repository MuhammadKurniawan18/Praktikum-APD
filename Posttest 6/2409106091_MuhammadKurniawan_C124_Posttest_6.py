# Inisialisasi data pengguna dan data buah
akun_pengguna = {}
data_buah = {}

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
        if Username in akun_pengguna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi 😁")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (penjual/pengguna): ").lower()
            if role not in ['penjual', 'pengguna']:
                print("Peran tidak valid. Harus 'admin' atau 'pengguna'.")
                continue
            akun_pengguna[Username] = {'password': Password, 'role': role, 'buah': []}  # Simpan username, password, dan data buah (sebagai dictionary kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username} 😁")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:
            while True:
                print(f"\nSelamat datang {Username}!")
                print("―――Silakan pilih langkah yang kamu mau 😊!―――")
                if akun_pengguna[Username]['role'] == 'penjual': 
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
                    if akun_pengguna[Username]['role'] == 'penjual':
                        jenis_buah = input("Jenis buah: ")
                        harga_buah = input("Harga buah: ")
                        berat_buah = input("Berat buah (Kg): ")
                        data_buah[jenis_buah] = {'harga': harga_buah, 'berat': berat_buah}  # Menambahkan data buah ke dalam dictionary
                        print("Data buah berhasil ditambahkan!\n")
                    else: 
                        jenis_buah = input("Jenis buah: ")
                        if jenis_buah in data_buah:
                            akun_pengguna[Username]['buah'].append({'jenis': jenis_buah, 'harga': data_buah[jenis_buah]['harga'], 'berat': data_buah[jenis_buah]['berat']}) #menambahkan buah ke dalam list
                            print("Buah berhasil dibeli!\n")
                        else:
                            print("buah tidak tersedia.\n")

                elif status == "2":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        for jenis, data in data_buah.items():
                            print(f"Jenis buah: {jenis}\nHarga buah: {data['harga']}\nBerat Buah: {data['berat']} Kg\n")
                        if not data_buah:
                            print("Opps, saat ini kamu belum punya data buah, silahkan tambah data buah terlebih dahulu.\n")
                    else:
                        for buah in akun_pengguna[Username]['buah']:
                            print(f"Jenis buah: {buah['jenis']}\nHarga buah: {buah['harga']}\nBerat Buah: {buah['berat']} Kg\n")
                        if not akun_pengguna[Username]['buah']:
                            print("Opps, saat ini kamu belum punya buah, silahkan beli buah terle bih dahulu.\n")

                elif status == "3":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        if not data_buah:
                            print("Tidak ada data buah yang bisa diedit.")
                        else:
                            edit = input("Jenis buah yang ingin kamu edit: ")
                            if edit in data_buah:
                                jenis_baru = input("Masukkan jenis yang baru: ")
                                harga_baru = input("Masukkan harga yang baru: ")
                                berat_baru = input("Masukkan berat yang baru (Kg): ")
                                print("Apa kamu yakin ingin mengedit data buah ?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    data_buah[edit] = {'harga': harga_baru, 'berat': berat_baru}  # Mengedit data buah
                                    print("Data buah yang kamu pilih sudah di edit ya!\n")
                                elif memastikan_edit == "2":
                                    print("Aksi untuk mengedit data buah dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada jenis buah yang kamu maksud, silahkan input ulang.\n")

                elif status == "4":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        if not data_buah:
                            print("Tidak ada data buah yang bisa dihapus.")
                        else:
                            hapus = input("Jenis buah yang ingin dihapus: ")
                            if hapus in data_buah:
                                print(f"Apa kamu yakin ingin menghapus data buah ? ")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del data_buah[hapus]  # Menghapus data buah dari dictionary
                                    print("Data buah yang kamu pilih sudah dihapus!\n")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus data buah dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada jenis buah yang kamu maksud, silahkan input ulang.\n")

                elif status == "5":
                    print("Aplikasi List Pembelian Buah ditutup.\n")
                    break

                else:
                    print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
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