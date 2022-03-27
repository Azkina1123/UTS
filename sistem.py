# TEMPATNYA FUNGSI-FUNGSI DAN PENYIMPANAN

import os
import time
import datetime as dt
import random

class Toko:
    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, password, lokasi):
        # identitas toko
        self.nama = nama
        self.password = password
        self.lokasi = lokasi

        # persediaan toko
        self.list_masker = [
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
        ] # tempat objek masker yg dijual

        self.list_pesanan = []
        self.pesanan_masuk = len(self.list_pesanan)
        self.pendapatan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def tambah_masker_baru(self, nama_masker, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, harga, jumlah))

    def tambah_pesanan_masuk(self, pembeli, nama_masker, jumlah, alamat):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                # persediaan masker dikurangi
                masker.kurangi_stok(jumlah)

                pesanan = [hari_ini(), pembeli, masker, jumlah, alamat]
                self.list_pesanan.append(pesanan)

                self.pendapatan += jumlah * masker.harga

    def kirim_masker(self, nomor, jumlah):
        pembeli = self.list_pesanan[nomor-1][1]
        masker = self.list_pesanan[nomor-1][2]
        index_masker = self.list_masker.index(masker)
        self.list_masker[index_masker].kurangi_stok(jumlah)

        pembeli.list_pesanan.pop(nomor)
        
    
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

    def tampilkan_pesanan(self):
        for i in range(len(self.list_pesanan)):
            tgl = self.list_pesanan[i][0]
            nama_pembeli = self.list_pesanan[i][1].nama
            nama_masker = self.list_pesanan[i][2]
            jumlah = self.list_pesanan[i][3]
            alamat = self.list_pesanan[i][4]

            print(f"({i}). {tgl}\t{nama_masker} x {jumlah}\n\t{alamat}")


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
                no_pesanan = 123
                toko.tambah_pesanan_masuk(self, kode, jumlah, alamat)
                self.list_pesanan.append([hari_ini(), masker, jumlah, ])

    def tampilkan_pesanan(self):
        for i in range(len(self.list_pesanan)):
            tanggal = self.list_pesanan[i][0]
            masker = self.list_pesanan[i][1]
            jumlah = self.list_pesanan[i][2]
            print(f"({i+1}). {tanggal}\t{masker.nama} x {jumlah}\tRp{masker.harga*jumlah}", end="")

# ==========================================================
#                           DATA 
# ==========================================================

akun_toko = [
    Toko(
        nama = "FORTRAN",
        password = "F0rtR355",
        lokasi = "Samarinda"
    )
]

daftar_masker = akun_toko[0].list_masker

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

def hari_ini():
    tanggal_hari_ini = dt.date.today()
    tanggal = tanggal_hari_ini.strftime("%d")
    bulan = tanggal_hari_ini.strftime("%m")
    tahun = tanggal_hari_ini.strftime("%Y") 

    return f"{tanggal}/{bulan}/{tahun}"

def tclear(sec):
    time.sleep(sec)
    clear()

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

# return Boolean
def jumlah_masuk_akal(jumlah):
    if jumlah > 0:
        return True
    else:
        return False

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

def insertion_sort(list_data):

    list_copy = list_data.copy()
    for i in range(1, len(list_copy)):
 
        key = list_data[i]

        j = i-1
        while j >=0 and key < list_data[j] :
                list_data[j+1] = list_data[j]
                j -= 1
        list_data[j+1] = key

def sort_berdasarkan(kategori):
    if kategori == "harga":
        list_harga = [masker.harga for masker in daftar_masker]
        print(list_harga)
        insertion_sort(list_harga)

        list_masker = sort_berdasarkan("nama")

        for i in range(len(list_harga)):
            for masker in list_masker:
                if list_harga[i] == masker.harga:
                    list_harga[i] = masker
                    list_masker.remove(masker)
        
        return list_harga

    elif kategori == "nama":
        list_nama = [masker.nama for masker in daftar_masker]
        insertion_sort(list_nama)

        for nama in list_nama:
            index_nama = list_nama.index(nama)

            for masker in daftar_masker:
                if nama == masker.nama:
                    list_nama[index_nama] = masker
        
        return list_nama

    elif kategori == "warna":
        list_warna = [masker.warna for masker in daftar_masker]
        print(list_warna)
        insertion_sort(list_warna)

        list_masker = sort_berdasarkan("nama")

        for i in range(len(list_warna)):
            for masker in list_masker:
                if list_warna[i] == masker.warna:
                    list_warna[i] = masker
                    list_masker.remove(masker)
        
        return list_warna
    
    elif kategori == "stok":
        list_stok = [masker.jumlah for masker in daftar_masker]
        print(list_stok)
        insertion_sort(list_stok)

        list_masker = sort_berdasarkan("nama")

        for i in range(len(list_stok)):
            for masker in list_masker:
                if list_stok[i] == masker.jumlah:
                    list_stok[i] = masker
                    list_masker.remove(masker)
        
        return list_stok


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
    return f"\033[{FontNumber};{ColourNumber};40m{text}\033[0m"

def printc(ColourCode, text, fonteu):
    print(Palette_Warna(ColourCode, text, fonteu))
