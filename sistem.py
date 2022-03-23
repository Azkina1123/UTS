
class Toko:

    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, lokasi):
        # identitas toko
        self.nama = nama
        self.lokasi = lokasi

        # persediaan toko
        self.list_masker = [] # tempat objek masker yg dijual
        self.pendapatan = 0
        self.pesanan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def tambah_masker_baru(self, nama_masker, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, harga, jumlah))

    def kirim_masker(self, nama_masker, jumlah):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                masker.jumlah -= jumlah
    
    def stok_masker(self, nama_masker):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                return masker.jumlah

    def stok_toko(self):
        if len(self.list_masker) != 0:
            for masker in self.list_masker:
                print(f"{masker.nama} saat ini = {masker.jumlah} buah")
        else:
            print("Toko belum memiliki barang yang bisa dijual.")


class Masker:
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

        # rating pembelian barang
        self.nilai = 0
        self.terjual = 0
        self.rate = self.nilai/self.terjual if self.terjual != 0 else 0

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_persediaan(self, jumlah):
        self.jumlah += jumlah

    def kurangi_persediaan(self, jumlah):
        self.jumlah -= jumlah


class Pembeli:
    # default attribute/properties tiap2 akun pembeli ------------------------
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, nama_masker, jumlah):
        for masker in toko.list_masker:
            if masker.nama == nama_masker:
                masker.jumlah -= jumlah
                masker.terjual += jumlah

    # 1 s/d 5
    def nilai_masker(self, toko, nama_masker, nilai):
        for masker in toko.list_masker:
            if masker.nama == nama_masker:
                masker.nilai += nilai

# contoh ----------------------------------------------------

# buat toko ......................
toko_ayam = Toko("Ayam", "Samarinda") # nama toko = Ayam, lokasi = Samarinda
#????????????????????????????????????????????????????????????#

# cek persediaan awal toko
print("Cek persediaan...")
toko_ayam.stok_toko()

print("\nTambah masker yang akan dijual...")
toko_ayam.tambah_masker_baru("Masker Biru", 1000, 100)
# nama masker = Masker Biru, harga = 1000, persediaan = 100

toko_ayam.tambah_masker_baru("Masker Hijau", 2000, 50)
# nama masker = Masker Hijau, harga = 2000, persediaan = 50

# cek persediaan toko
print("\nCek persediaan...")
print("Stok Toko Ayam : ")
toko_ayam.stok_toko()


# buat akun pembeli ...................
yafi = Pembeli("Yafi", 123)
# nama pembeli = Yafi, password = 123

print("\nYapi pesan masker...")
# yapi beli Masker Biru 50 buah
yafi.pesan_masker(toko_ayam, "Masker Biru", 50)
# yapi beli Masker Biru dari Toko Ayam 30 buah
yafi.pesan_masker(toko_ayam, "Masker Hijau", 30)

# cek persediaan toko lagi
print("\nCek persediaan...")
print("Stok Toko Ayam : ")
toko_ayam.stok_toko()


# Menu?
def Menu_User():
    print("""\n\n\n\n\n
            !Selamat Datang!

      Masuk ke dalam program sebagai:
    [1] Pembeli            [2] Penjual""")

    Respon_Menu_User = int(input("\n\t\t >> "))
    if Respon_Menu_User == 1:
        #cls
        Login_Pembeli()
    elif Respon_Menu_User == 2:
        #cls
        Login_Penjual()
    else:
        print (f"Menu < {Respon_Menu_User} > tidak tersedia")
        #timed_cls
        Menu_User()

def Login_Pembeli():
    print("""\n\n\n\n\n


    Pilih metode masuk:
    [1] Login   [2] Sign-up
    """)
    Respon_menu_user = int(input("\n\t\t >> "))
    if Respon_menu_user == 1:
        print()
        #input(Nama)
        #input(Password)
        #Verifikasi nama+pass / pembatalan pilihan --> Login_Pembeli()
        #cls, Menu_untuk_pembeli()
    
    elif Respon_menu_user == 2:
        print()
        #input(Nama)
        #input(Password)
        #Verifikasi apakah nama sudah tersedia atau belum
        #cls, Login_Pembeli()

def Login_Penjual():
    print("""\n\n\n\n\n


    <Konfirmasi Identitas> """)
   #input(Nama)
   #input(Password)
   #Verifikasi nama+pass / pengusiran paksa


#------------------------- Menu Sebenarnya -------------------------#


def Menu_untuk_Pembeli(Notes="Selamat datang ((Pembeli))!!"):
    print(f""" {Notes}
    [1] Pilih kategori barang
    [2] Cari barang berdasarkan nama
    [3] Cek daftar barang secara keseluruhan
    [4] Menuju struk belanja
    [5] Keluar """)
    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    Respon_menu_user = int(input("\n\t\t>>"))
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

def Menu_pembeli_satu():
    #cls
    #pilih kategori(Nama, Warna)
    print()

def Menu_pembeli_dua():
    Barang_dituju = input("\n Masukkan nama barang: ")
    #cls
    #if Barang_dituju in ListBarang --> "\n\n\t\tbarang ditemukan!: ", tampilkan barang dan stok
    #Apakah ingin menambahkan ke kereta belanja?

    #if Barang_dituju not in ListBarang -->
    for i in range(3,0,-1):
        print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")
        #timed cls 1s


def Menu_pembeli_tiga():
    #Sort barang berdasarkan? (Nama, Warna, Stok, Best seller(?), harga)
    print()

Menu_User()

