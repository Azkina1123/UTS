# TEMPATNYA FUNGSI-FUNGSI

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

        self.list_pesanan_masuk = []
        self.pesanan_masuk = len(self.list_pesanan_masuk)
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
                self.list_pesanan_masuk.append(pesanan)

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
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, warna, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.warna = warna
        self.harga = harga
        self.jumlah = jumlah

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_stok(self, jumlah):
        self.jumlah += jumlah

    def kurangi_stok(self, jumlah):
        self.jumlah -= jumlah

    def tampilkan_data(self):
        print(
            f"Nama\t: {self.nama}\
            \nWarna\t: {self.warna}\
            \nHarga\t: {self.harga}\
            \nStok\t: {self.jumlah}"
        )


class Pembeli:
    # default attribute/properties tiap2 akun pembeli ------------------------
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, nama_masker, jumlah, alamat):
        for masker in toko.list_masker:
            if masker.nama == nama_masker:
                toko.tambah_pesanan_masuk(nama_masker, jumlah, alamat)

# ==========================================================
#                           DATA 
# ==========================================================

akun_toko = Toko(
    nama="Toko Masker",
    password="IS-IS",
    lokasi="Samarinda"
)

daftar_masker = [
    Masker(
        nama="Masker KF94 10 Pcs",
        warna="Putih", 
        harga=12000,
        jumlah=100
    ),
    Masker(
        nama="Masker KF94 50 Pcs",
        warna="Putih",
        harga=45000,
        jumlah=500
    )
]

akun_pembeli = [
    Pembeli(
        nama="Yafi",
        password="Yafi"
    ),
    Pembeli(
        nama="Iza",
        password="Iza"
    )
]

# =========================================================
#                          FUNGSI
# =========================================================

def clear():
    _ = os.system("cls")

def nama_sudah_ada(tipe_akun, nama):
    for akun in tipe_akun:
        if akun.nama == nama:
            return True
    else:
        return False

def password_benar(tipe_akun, nama, password):
    for akun in tipe_akun:
        if akun.nama == nama:
            if akun.password == password:
                return True
    else:
        return False

def masker_tersedia(nama):
    for masker in daftar_masker:
        if nama.casefold() in masker.nama.casefold():
            return True
    else:
        return False

def masker_dipilih(nama):
    for masker in daftar_masker:
        if nama.casefold() in masker.nama.casefold():
            return masker

def search():
    pass

def sort():
    pass


