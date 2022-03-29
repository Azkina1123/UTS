import sqlite3
import random
import datetime as dt

from sistem import *

def hari_ini():
    tanggal_hari_ini = dt.date.today()
    tanggal = tanggal_hari_ini.strftime("%d")
    bulan = tanggal_hari_ini.strftime("%m")
    tahun = tanggal_hari_ini.strftime("%Y") 

    return f"{tanggal}/{bulan}/{tahun}"

def nomor_pesanan(masker):
    char = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    ]
    no_pesanan = "FR" + masker.kode
    for i in range(5):
        random_char = str(random.choice(char))
        no_pesanan += random_char

    return no_pesanan

class Toko:
    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, password):
        
        # identitas toko
        self.nama = nama
        self.password = password

        # persediaan toko
        self.list_masker = [] # tempat objek masker yg dijual

        self.list_pesanan = []
        self.pesanan_masuk = len(self.list_pesanan)
        self.pendapatan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def konfigurasi_awal(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        select_masker = f'''SELECT * FROM tabel_masker'''
        list_masker = list(cur.execute(select_masker))

        for masker in list_masker:
            self.list_masker.append(Masker(masker[1], masker[2], masker[3], masker[4]))

        con.commit()
        con.close()

    def tambah_masker_baru(self, nama_masker, warna, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, warna, harga, jumlah))

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        # kode_masker, nama_masker, warna, harga, jumlah
        tambahkan_masker = f'''INSERT INTO tabel_masker VALUES (
            '{self.list_masker[len(self.list_masker)-1].kode}', 
            '{nama_masker}', 
            '{warna}', 
            {harga}, 
            {jumlah}
        )'''

        cur.execute(tambahkan_masker)
        con.commit()
        con.close()

        print(self.list_masker)

    def tambah_pesanan_masuk(self, no_pesanan, pembeli, masker, jumlah, alamat):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        # persediaan masker dikurangi
        masker.kurangi_stok(jumlah)

        # tanggal, no_pesanan, nama_masker, jumlah, total, nama_pembeli, alamat
        tambah_pesanan = f'''INSERT INTO tabel_pesanan_penjual VALUES (
            '{hari_ini()}', 
            '{no_pesanan}', 
            '{masker.nama}',
            '{jumlah}' 
            '{masker.harga*jumlah}',
            '{pembeli.nama}',
            '{alamat}'
        )'''

        cur.execute(tambah_pesanan)
        con.commit()
        con.close()

    def hapus_pesanan_masuk(self, no_pesanan):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        hapus_pesanan = f'''DELETE FROM tabel_pesanan_penjual 
                            WHERE nomor_pesanan = {no_pesanan}'''
        cur.execute(hapus_pesanan)

        con.commit()
        con.close()

    def kirim_pesanan(self, no_pesanan, jumlah):
        index_pesanan = fibonacci_search(
            list_data = [pesanan[1] for pesanan in self.list_pesanan],
            data = no_pesanan
        )

        nama_masker = self.list_pesanan[index_pesanan][2]
        index_masker = fibonacci_search(
            list_data = [masker.nama for masker in self.list_masker],
            data = nama_masker
        )

        self.list_masker[index_masker].kurangi_stok(jumlah) # kurangi stok
        self.hapus_pesanan_masuk(no_pesanan)                # hapus pesanan

    def tampilkan_pesanan(self):
        i = 1
        for pesanan in self.list_pesanan:
            tanggal = pesanan[0]
            no_pesanan = pesanan[1]
            nama_masker = pesanan[2]
            jumlah = pesanan[3]
            total = pesanan[4]
            pembeli = pesanan[5]
            alamat = pesanan[6]
            
            print(f"({i}). {tanggal} -- {no_pesanan}\
                \n\t{nama_masker} x {jumlah}\tRp{total}\
                \n\t{alamat} -- {pembeli.nama}")

            i += 1

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
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        tambah = f'''UPDATE tabel_masker 
        SET jumlah = {self.jumlah + jumlah}
        WHERE nama_masker = {self.nama}'''

        cur.execute(tambah)
        con.commit()
        con.close()

    def kurangi_stok(self, jumlah):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        kurangi = f'''UPDATE tabel_masker 
        SET jumlah = {self.jumlah - jumlah}
        WHERE nama_masker = {self.nama}'''

        cur.execute(kurangi)
        con.commit()
        con.close()

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
        self.list_pesanan = [pesanan for pesanan in akun_toko[0].list_pesanan if self.nama == pesanan[5]]
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, kode, jumlah, alamat):
        for masker in toko.list_masker:
            if masker.kode == kode:
                no_pesanan = nomor_pesanan(masker)
                toko.tambah_pesanan_masuk(no_pesanan, self, masker, jumlah, alamat)

    def tampilkan_pesanan(self):
        i = 1
        for pesanan in self.list_pesanan:
            tanggal = pesanan[0]
            no_pesanan = pesanan[1]
            nama_masker = pesanan[2]
            jumlah = pesanan[3]
            pembeli = pesanan[5]
            total = pesanan[4]
            alamat = pesanan[6]

            print(f"({i}). {tanggal} -- {no_pesanan}\
                \n\t{nama_masker} x {jumlah}\tRp{total}\
                \n\t{alamat} -- {pembeli.nama}")
            i += 1


# toko.tambah_masker_baru("Gojek", "Hitam", 123, 100)

akun_toko = [
    Toko(
        nama = "F",
        password = "123"
    )
]

daftar_masker = akun_toko[0].list_masker

akun_pembeli = [
    Pembeli(
        nama="Yapoy",
        password="Yapoy"
    ),
    Pembeli(
        nama="zz",
        password="zz"
    )
]
