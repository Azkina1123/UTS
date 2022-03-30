# TEMPATNYA FUNGSI-FUNGSI DAN PENYIMPANAN

#from curses.ascii import isspace
import os
from select import select
import time
import datetime as dt
import random
import sqlite3

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
    def tambah_masker_baru(self, nama_masker, warna, harga, jumlah, kode):
        self.list_masker.append(Masker(nama_masker, warna, harga, jumlah, kode))
        
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        # kode_masker, nama_masker, warna, harga, jumlah
        tambahkan_masker = f'''INSERT INTO tabel_masker VALUES (
            '{kode}', 
            '{nama_masker}', 
            '{warna}', 
            {harga}, 
            {jumlah}
        )'''

        cur.execute(tambahkan_masker)
        con.commit()
        con.close()

        update_toko()

    def hapus_masker(self, kode):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        hapus = f"""DELETE FROM tabel_masker
                    WHERE kode = '{kode}'"""
        cur.execute(hapus)

        con.commit()
        con.close()

        update_toko()

    def restok_masker(self, mode, kode, jumlah):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        select_data = """SELECT * FROM tabel_masker"""
        list_masker = list(cur.execute(select_data))
        print(list_masker)
        input("=====================")

        for masker in list_masker:
            if masker[0] == kode:
                if mode == "tambah":
                    input("Masukk?????")
                    tambah = f"""UPDATE tabel_masker 
                    SET jumlah = {masker[4] + jumlah}
                    WHERE kode = '{kode}'"""
                    cur.execute(tambah)
                else:
                    kurang = f"""UPDATE tabel_masker 
                    SET jumlah = {masker[4] - jumlah}
                    WHERE kode = '{kode}'"""
                    cur.execute(kurang)
        con.commit()
        con.close()
        update_toko()

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
            {jumlah},
            {masker.harga*jumlah},
            '{pembeli.nama}',
            '{alamat}',
            'belum dikirim'
        )'''

        cur.execute(tambah_pesanan)
        con.commit()
        con.close()

        update_toko()

    def hapus_pesanan_masuk(self, no_pesanan):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        hapus_pesanan = f"""DELETE FROM tabel_pesanan_penjual 
                            WHERE nomor_pesanan = '{no_pesanan}'"""
        cur.execute(hapus_pesanan)

        con.commit()
        con.close()

        update_toko()

    def kirim_masker(self, no_pesanan):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        # update database
        update_status = f"""UPDATE tabel_pesanan_penjual
                            SET status = 'sudah dikirim'
                            WHERE nomor_pesanan = '{no_pesanan}'"""
        cur.execute(update_status)

        con.commit()
        con.close()

        update_toko()

    def tampilkan_pesanan(self):
        i = 1
        for pesanan in self.list_pesanan:
            tanggal = pesanan[0]
            no_pesanan = pesanan[1]
            nama_masker = pesanan[2]
            jumlah = pesanan[3]
            total = pesanan[4]
            nama_pembeli = pesanan[5]
            alamat = pesanan[6]
            status = pesanan[7]
            
            print(f"({i}). {tanggal} -- {no_pesanan}\
                \n\t{nama_masker} x {jumlah}\tRp{total}\
                \n\t{alamat} -- {nama_pembeli}\
                \n\t\t -- {status}")

            i += 1

class Masker:
    jumlah_seluruh_masker = 0
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, warna, harga, jumlah, kode):
        # identitas barang
        self.nama = nama
        self.warna = warna
        self.harga = harga
        self.jumlah = jumlah
        self.kode = kode
        Masker.jumlah_seluruh_masker += 1

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_stok(self, jumlah):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        tambah = f"""UPDATE tabel_masker 
        SET jumlah = {self.jumlah + jumlah}
        WHERE kode = '{self.kode}'"""

        cur.execute(tambah)
        con.commit()
        con.close()

        update_toko()

    def kurangi_stok(self, jumlah):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        kurangi = f"""UPDATE tabel_masker 
        SET jumlah = {self.jumlah - jumlah}
        WHERE nama_masker = '{self.kode}'"""

        cur.execute(kurangi)
        con.commit()
        con.close()

        update_toko()

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
            nama_pembeli = pesanan[5]
            total = pesanan[4]
            alamat = pesanan[6]
            status = pesanan[7]

            print(f"({i}). {tanggal} -- {no_pesanan}\
                \n\t{nama_masker} x {jumlah}\tRp{total}\
                \n\tAlamat  : {alamat}\
                \n\tPembeli : {nama_pembeli}\
                \n\t\t -- {status}")
            i += 1

    def update_pesanan(self):
        self.list_pesanan = [pesanan for pesanan in akun_toko[0].list_pesanan if self.nama == pesanan[5]]

# =========================================================
#                           DATA
# =========================================================

akun_toko = [
    Toko(
        nama = "F",
        password = "123"
    )
]

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

# =========================================================
#                          FUNGSI
# =========================================================

def clear():
    _ = os.system("cls")


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
    for masker in akun_toko[0].list_masker:
        if nama.casefold() in masker.nama.casefold() and nama.isspace() != True and nama != "" or\
            nama.casefold() in masker.warna.casefold() and nama.isspace() != True and nama != "":
            return True
    else:
        return False

# return Masker
def masker_dipilih(nama):
    # cari nama yg berkaitan dgn yg dicari
    nama_ditemukan = []
    for masker in akun_toko[0].list_masker:
        if nama.casefold() in masker.nama.casefold():
            nama_ditemukan.append(masker.nama)

    # list nama semua masker yg tersedia
    list_nama_masker = [masker.nama for masker in akun_toko[0].list_masker]
    
    # cari masker2 yg ditemukan
    masker_ditemukan = []
    for nama_masker in nama_ditemukan:
        index = fibonacci_search(list_nama_masker, nama_masker)
        masker_ditemukan.append(akun_toko[0].list_masker[index])

    return masker_ditemukan

# return Boolean
def jumlah_masuk_akal(jumlah):
    try:
        if jumlah > 0:
            return True
        else:
            return False
    except:
        return False

# sort n search ...........................................................
# return int atau None
def fibonacci_search(list_data, data):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(list_data)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(list_data)-1))
        if (list_data[i] < data):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (list_data[i] > data):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(list_data)-1) and list_data[index+1] == data):
        return index+1
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
        list_harga = [masker.harga for masker in akun_toko[0].list_masker]
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
        list_nama = [masker.nama for masker in akun_toko[0].list_masker]
        insertion_sort(list_nama)

        for nama in list_nama:
            index_nama = list_nama.index(nama)

            for masker in akun_toko[0].list_masker:
                if nama == masker.nama:
                    list_nama[index_nama] = masker
        
        return list_nama

    elif kategori == "warna":
        list_warna = [masker.warna for masker in akun_toko[0].list_masker]
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
        list_stok = [masker.jumlah for masker in akun_toko[0].list_masker]
        print(list_stok)
        insertion_sort(list_stok)

        list_masker = sort_berdasarkan("nama")

        for i in range(len(list_stok)):
            for masker in list_masker:
                if list_stok[i] == masker.jumlah:
                    list_stok[i] = masker
                    list_masker.remove(masker)
        
        return list_stok

# pesanan ..................................................................
def hari_ini():
    tanggal_hari_ini = dt.date.today()
    tanggal = tanggal_hari_ini.strftime("%d")
    bulan = tanggal_hari_ini.strftime("%m")
    tahun = tanggal_hari_ini.strftime("%Y") 

    return f"{tanggal}/{bulan}/{tahun}"

char = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
def nomor_pesanan(masker):

    no_pesanan = masker.kode
    for i in range(5):
        random_char = str(random.choice(char))
        no_pesanan += random_char

    return no_pesanan

def kode_masker(num, warna):
    return f"ms{num}{warna[0]}"

# decorating material ......................................................
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

def inputc(ColourCode, text, fonteu):
    return input(f"{Palette_Warna(ColourCode, text, fonteu)}")



# UPDATE PENYIMPANAN
def update_toko():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    select_masker = f'''SELECT * FROM tabel_masker'''
    list_masker = list(cur.execute(select_masker))

    akun_toko[0].list_masker.clear()
    for masker in list_masker:
        akun_toko[0].list_masker.append(
            Masker(
                nama = masker[1],
                warna = masker[2],
                harga = masker[3],
                jumlah = masker[4],
                kode = masker[0]
            )
        )

    select_pesanan = f'''SELECT * FROM tabel_pesanan_penjual'''
    list_pesanan = list(cur.execute(select_pesanan))
    akun_toko[0].list_pesanan = list_pesanan

    for pembeli in akun_pembeli:
        pembeli.update_pesanan()

    con.commit()
    con.close()

def akun_pembali_baru(nama, password):
    global akun_pembeli

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    tambah_akun = f'''INSERT INTO tabel_akun_pembeli
            (nama, password) VALUES
            ('{nama}', '{password}')'''

    cur.execute(tambah_akun)

    select_akun = '''SELECT * FROM tabel_akun_pembeli'''
    list_akun = list(cur.execute(select_akun))

    akun_pembeli = []
    for akun in list_akun:
        nama, password = akun
        akun_pembeli.append(
            Pembeli(
                nama = nama,
                password= password
            )
        )

    con.commit()
    con.close()


    