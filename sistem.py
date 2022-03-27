# TEMPATNYA FUNGSI-FUNGSI DAN PENYIMPANAN

import os

class Toko:
    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, password, lokasi):
        # identitas toko
        self.nama = nama
        self.password = password
        self.lokasi = lokasi

        # persediaan toko
        self.list_masker = [] # tempat objek masker yg dijual

        self.list_pesanan = []
        self.pesanan_masuk = len(self.list_pesanan)
        self.pendapatan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def tambah_masker_baru(self, nama_masker, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, harga, jumlah))

    def tambah_pesanan_masuk(self, nama_masker, jumlah, alamat):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                # persediaan masker dikurangi
                masker.kurangi_stok(jumlah)

                pesanan = [nama_masker, jumlah, alamat]
                self.list_pesanan.append(pesanan)

                self.pendapatan += jumlah * masker.harga

    def kirim_masker(self):
        pass
    
    def restock_masker(self, nama_masker, jumlah):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                masker.tambah_stok(jumlah)
    
    def stok_masker(self, nama_masker):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                return masker.jumlah

    def stok_toko(self):
        if len(self.list_masker) != 0:
            for masker in self.list_masker:
                print(f"{masker.nama} saat ini = {masker.jumlah} buah")
        else:
            print("Toko belum memiliki barang yang dijual.")


class Masker:
    jumlah_seluruh_masker = 0
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, warna, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.warna = warna
        self.harga = harga
        self.jumlah = jumlah
        Masker.jumlah_seluruh_masker += 1
        self.kode = f"ms{Masker.jumlah_seluruh_masker}"

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_stok(self, jumlah):
        self.jumlah += jumlah

    def kurangi_stok(self, jumlah):
        self.jumlah -= jumlah

    def tampilkan_data(self):
        print(
            f"[{self.kode.center(30)}]\
            \nNama\t: {self.nama}\
            \nWarna\t: {self.warna}\
            \nHarga\t: Rp{self.harga}\
            \nStok\t: {self.jumlah}"
        )


class Pembeli:
    # default attribute/properties tiap2 akun pembeli ------------------------
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
        self.list_pesanan = []
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, kode, jumlah, alamat):
        for masker in toko.list_masker:
            if masker.kode == kode:
                toko.tambah_pesanan_masuk(kode, jumlah, alamat)
                self.list_pesanan.append(masker)

# ==========================================================
#                           DATA 
# ==========================================================

akun_toko = [
    Toko(
        nama = "FORTRAN",
        password = "YAPIZ",
        lokasi = "Samarinda"
    )
]

daftar_masker = [
    Masker(
        nama = "Masker KF94 10 Pcs",
        warna = "Putih", 
        harga = 12000,
        jumlah = 100
    ),
    Masker(
        nama = "Masker KF94 50 Pcs",
        warna = "Putih",
        harga = 45000,
        jumlah = 500
    ),
    Masker(
        nama = "Masker KN95 10 Pcs",
        warna = "Putih",
        harga = 10000,
        jumlah = 150
    ),
    Masker(
        nama = "Masker KN95 50 Pcs",
        warna = "Putih",
        harga = 40000,
        jumlah = 500
    )
]

for i in range(1):
    daftar_masker[i].tampilkan_data()


akun_pembeli = [
    Pembeli(
        nama="Yapoy",
        password="Yapoy"
    ),
    Pembeli(
        nama="Haji ijah",
        password="Haji Ijah"
    )
]

# =========================================================
#                          FUNGSI
# =========================================================

def clear():
    _ = os.system("cls")

# return Boolean
def nama_sudah_ada(tipe_akun, nama):
    for akun in tipe_akun:
        if akun.nama == nama:
            return True
    else:
        return False

# return Boolean
def password_benar(tipe_akun, nama, password):
    for akun in tipe_akun:
        if akun.nama == nama:
            if akun.password == password:
                return True
    else:
        return False

# return Boolean
def masker_tersedia(nama):
    for masker in daftar_masker:
        if nama.casefold() in masker.nama.casefold():
            return True
    else:
        return False

# return Masker
def masker_dipilih(nama):
    # cari nama yg berkaitan dgn yg dicari
    nama_ditemukan = []
    for masker in daftar_masker:
        if nama.casefold() in masker.nama.casefold():
            nama_ditemukan.append(masker.nama)

    # list nama semua masker yg tersedia
    list_nama_masker = [masker.nama for masker in daftar_masker]
    
    # cari masker2 yg ditemukan
    masker_ditemukan = []
    for nama_masker in nama_ditemukan:
        index = fibonacci_search(list_nama_masker, nama_masker)
        masker_ditemukan.append(daftar_masker[index])

    return masker_ditemukan

# return int atau None
def fibonacci_search(list_data, data):
    size = len(list_data)
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if list_data[index] < data:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif list_data[index] > data:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (list_data[size - 1] == data):
        return size - 1
    return None

def sort():
    pass

def is_integer(angka):
    try:
        int(angka)
    except ValueError:
        return False
    else:
        return True 

# decorating material

def Palette_Warna(ColourCode="White", text="", fonteu="Reset"):
    ColourTupleA = ("Black","Red","Green","Orange","Blue","Purple","Cyan","White")
    ColourTupleB = ("Grey","LRed","LGreen","Yellow","LBlue","Pink","LCyan")
    FontTuple = ("Reset","Bold","Disable",0,"Underline",0,0,"Reverse","Invisible","Strikethrough")

    if ColourCode in ColourTupleA:
        ColourNumber = 30 + ColourTupleA.index(ColourCode)
    elif ColourCode in ColourTupleB:
        ColourNumber = 90 + ColourTupleB.index(ColourCode)
    FontNumber = FontTuple.index(fonteu)
    return f"\033[{FontNumber};{ColourNumber};40m{text}"

def printc(ColourCode, text, fonteu):
    print(Palette_Warna(ColourCode, text, fonteu))
