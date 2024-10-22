from prettytable import PrettyTable

# Inisialisasi data pengguna dan data buah
akun_pengguna = {
    "penjual": {'password': '1', 'role': 'penjual', 'pembelian': []},
    "pelanggan": {'password': '2', 'role': 'pelanggan', 'pembelian': []}
}

data_buah = {
    "Apel": {'harga': '20000', 'stok': 50},
    "Naga": {'harga': '30000', 'stok': 20},
    "Jeruk": {'harga': '15000', 'stok': 80},
    "Nipah": {'harga': '30000', 'stok': 20},
    "Melon": {'harga': '25000', 'stok': 10},
    "Nanas": {'harga': '20000', 'stok': 17},
    "Pisang": {'harga': '10000', 'stok': 50},
    "Anggur": {'harga': '20000', 'stok': 27},
    "Mangga": {'harga': '25000', 'stok': 30},
    "Durian": {'harga': '60000', 'stok': 10},
    "Pepaya": {'harga': '12000', 'stok': 19},
    "Alpukat": {'harga': '11000', 'stok': 40},
    "Semangka": {'harga': '20000', 'stok': 21},
    "Kedondong": {'harga': '10000', 'stok': 60},
    "Kelengkeng": {'harga': '12000', 'stok': 23},
    "Strawberry": {'harga': '10000', 'stok': 30}

}


# Adding Color
class style():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'
    
    CBLACK  = '\33[30m'
    CRED    = '\33[31m' 
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'
    
    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'
    
    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'
    
    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

    
# Global variables
total_buah = len(data_buah)
total_pembelian = 0
total_pendapatan = 0

def tampilkan_menu():
    print(style.CBLUE2 + """
    ═════════════════════════════════════════════════════════
        Selamat Datang Di Aplikasi Pembelian Buah
            Silahkan Pilih Opsi Sign-In atau Sign-Up
            
        1.   Daftar Akun
        2.   Login
        3.   Exit
        
    ═════════════════════════════════════════════════════════
          """)

def registrasi_akun():
    print(style.CGREEN2 + "Halo pelanggan baru! Ayo buat akun dulu")
    Username = input("Username: ")
    if Username in akun_pengguna:
        print(style.CRED2 + "Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
    else:
        Password = input("Password: ")
        role = input("Masukkan peran (penjual/pelanggan): ").lower()
        if role not in ['penjual', 'pelanggan']:
            print(style.CRED2 + "Peran tidak valid. Harus 'penjual' atau 'pelanggan'.")
            return
        akun_pengguna[Username] = {'password': Password, 'role': role, 'pembelian': []}
        print(style.CGREEN2 + f"Akun Anda berhasil terdaftar dengan ID: {Username}")

def login_akun():
    print(style.CYELLOW2 + "Hi, Silahkan login dulu ya!")   
    Username = input("Username: ")
    Password = input("Password: ")
    if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:
        return Username
    else:
        print(style.CRED2 + "Username dan password anda salah, silahkan coba lagi\n")
        return None

def tampilkan_menu_penjual(Username):
    print(style.CGREEN2 + f"""
    ═════════════════════════════════════════════════════════
        Penjualan Buah
        {Username} Di Menu Penjual
            
        1.   Tambah Buah
        2.   Lihat Buah
        3.   Edit Buah
        4.   Hapus Buah
        5.   Exit
        
    ═════════════════════════════════════════════════════════
          """)

def tampilkan_menu_pengguna(Username):
    print(style.CVIOLET2 + f"""
    ═════════════════════════════════════════════════════════
        Penjualan Buah
        {Username} Di Menu Pengguna
            
        1.   Beli Buah
        2.   Lihat Pembelian Yang Sudah Dilakukan
        5.   Exit
        
    ═════════════════════════════════════════════════════════
          """)

def tambah_buah():
    global total_buah
    nama_buah = input("Nama Buah: ")
    harga_buah = input("Harga Buah: ")
    stok_buah = int(input("Stok Buah: "))
    data_buah[nama_buah] = {'harga': harga_buah, 'stok': stok_buah}
    total_buah += 1
    print(style.CGREEN2 + "Buah berhasil ditambahkan!\n")

def lihat_buah():
    table = PrettyTable()
    table.field_names = ["Nama Buah", "Harga Buah", "Stok Buah"]
    for nama, buah in data_buah.items():
        table.add_row([nama, buah['harga'], buah['stok']])
    print(table)

def edit_buah():
    if not data_buah:
        print(style.CRED2 + "Tidak ada buah yang bisa diedit.")
    else:
        print("Daftar Buah:")
        for i, (nama, buah) in enumerate(data_buah.items()):
            print(f"{i+1}. {nama}")
        edit = int(input("Masukkan nomor buah yang ingin diedit: ")) - 1
        if 0 <= edit < len(data_buah):
            nama_buah = list(data_buah.keys())[edit]
            nama_baru = input("Masukkan nama yang baru: ")
            harga_baru = input("Masukkan harga yang baru: ")
            stok_baru = int(input("Masukkan stok yang baru: "))
            print("Apa kamu yakin ingin mengedit buah ? ")
            print("1. Iya")
            print("2. Tidak")
            memastikan_edit = input("Pilih: ")
            if memastikan_edit == "1":
                del data_buah[nama_buah]
                data_buah[nama_baru] = {'harga': harga_baru, 'stok': stok_baru}
                print(style.CGREEN2 + "Buah yang kamu pilih sudah di edit ya!\n")
            elif memastikan_edit == "2":
                print(style.CRED2 + "Aksi untuk mengedit buah dibatalkan")
            else:
                print(style.CRED2 + "Mohon pilih '1' atau '2'")
        else:
            print(style.CRED2 + "Tidak ada nomor buah yang kamu maksud, silahkan input ulang.\n")

def hapus_buah():
    global total_buah
    if not data_buah:
        print("Tidak ada buah yang bisa dihapus.")
    else:
        hapus = input("Masukkan nama buah yang ingin dihapus: ")
        if hapus in data_buah:
            print(f"Apa kamu yakin ingin menghapus buah ? ")
            print("1. Iya")
            print("2. Tidak")
            memastikan_hapus = input("Pilih: ")
            if memastikan_hapus == "1":
                del data_buah[hapus]
                total_buah -= 1
                print("Buah yang kamu pilih sudah dihapus!\n")
            elif memastikan_hapus == "2":
                print("Aksi untuk menghapus buah dibatalkan")
            else:
                print("Mohon pilih '1' atau '2'")
        else:
            print("Tidak ada buah yang kamu maksud, silahkan input ulang.\n")

def beli_buah(Username):
    global total_pembelian, total_pendapatan
    for nama, buah in data_buah.items():
        print(style.CGREEN2 + f"Nama Buah: {nama}\nHarga Buah: {buah['harga']}\nStok Buah: {buah['stok']}\n")
    nama_buah = input("Nama Buah: ")
    if nama_buah in data_buah:
        if data_buah[nama_buah]['stok'] > 0:
            akun_pengguna[Username]['pembelian'].append({'nama': nama_buah, 'harga': data_buah[nama_buah]['harga']})
            data_buah[nama_buah]['stok'] -= 1
            total_pembelian += 1
            total_pendapatan += int(data_buah[nama_buah]['harga'].replace('Rp ', ''))
            print(style.CGREEN2 + "Buah berhasil dibeli!\n")
        else:
            print(style.CRED2 + "Stok buah habis.\n")
    else:
        print(style.CRED2 + "Buah tidak tersedia.\n")

def lihat_pembelian(Username):
    for pembelian in akun_pengguna[Username]['pembelian']:
        print(style.CGREEN2 + f"Nama Buah: {pembelian['nama']}\nHarga Buah: {pembelian['harga']}\n")
    if not akun_pengguna[Username]['pembelian']:
        print(style.CRED2 + "Opps, saat ini kamu belum punya pembelian, silahkan beli buah terlebih dahulu.\n")

def lihat_statistik():
    print(style.CGREEN2 + f"Total Buah: {total_buah}")
    print(style.CGREEN2 + f"Total Pembelian: {total_pembelian}")
    print(style.CGREEN2 + f"Total Pendapatan: Rp {total_pendapatan}")

while True:
    tampilkan_menu()
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        registrasi_akun()
    elif opsi == "2":
        Username = login_akun()
        if Username:
            while True:
                if akun_pengguna[Username]['role'] == 'penjual':
                    tampilkan_menu_penjual(Username)
                else:
                    tampilkan_menu_pengguna(Username)
                status = input("Pilih opsi: ")
                print(" ")

                if status == "1":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        tambah_buah()
                    else:
                        beli_buah(Username)
                elif status == "2":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        lihat_buah()
                    else:
                        lihat_pembelian(Username)
                elif status == "3":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        edit_buah()
                    else:
                        print("Anda tidak memiliki akses untuk mengedit buah.\n")
                elif status == "4":
                    if akun_pengguna[Username]['role'] == 'penjual':
                        hapus_buah()
                    else:
                        print("Anda tidak memiliki akses untuk menghapus buah.\n")
                elif status == "5":
                        print("Aplikasi Pembelian Buah ditutup.\n")
                        break
                else:
                    print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
        else:
            continue
    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")