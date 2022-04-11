# TEMPATNYA FUNGSI-FUNGSI DAN PENYIMPANAN

#from curses.ascii import isspace
import os
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
        self.list_masker.append(
            Masker(nama_masker, warna, harga, jumlah, kode)
        )
        
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

        for masker in list_masker:
            if masker[0] == kode:
                if mode == "tambah":
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

        # tanggal, no_pesanan, nama_masker, jumlah, total, nama_pembeli, alamat
        tambah_pesanan = f'''INSERT INTO tabel_pesanan_penjual VALUES (
            '{hari_ini()}',
            '{no_pesanan}', 
            '{masker.nama}',
            '{masker.warna}',
            {jumlah},
            {masker.harga*jumlah},
            '{pembeli.nama}',
            '{alamat}',
            '{"belum dikirim"}'
        )'''

        cur.execute(tambah_pesanan)
        con.commit()
        con.close()

        # persediaan masker dikurangi
        self.restok_masker(
            "kurang", 
            masker.kode,
            jumlah
        )

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
            warna = pesanan[3]
            jumlah = pesanan[4]
            total = pesanan[5]
            nama_pembeli = pesanan[6]
            alamat = pesanan[7]
            status = pesanan[8]

            if status == "belum dikirim":
                status = Palette_Warna("Yellow", "belum dikirim")
            else:
                status = "\033[4;95;40m" + status + "\033[0m"
            
            print(f"\t\t   ({i}). {tanggal} -- [{no_pesanan}]\
                \n\t\t\tMasker  : {nama_masker} x {jumlah}\
                \n\t\t\tWarna   : {warna} {identify_warna(warna)}\
                \n\t\t\tHarga   : Rp{total}\
                \n\t\t\tAlamat  : {alamat}\
                \n\t\t\tPembeli : {nama_pembeli}\
                \n\t\t\t\t -- {status}\n")

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
            f"\t\t\t   [{self.kode.center(30)}]\
            \n\t\t\t| \033[1mNama\t:\033[0m {self.nama}\
            \n\t\t\t| \033[1mWarna\t:\033[0m {self.warna} {identify_warna(self.warna)}\
            \n\t\t\t| \033[1mHarga\t:\033[0m Rp{self.harga}\
            \n\t\t\t| \033[1mStok\t:\033[0m {self.jumlah}"
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
            warna = pesanan[3]
            jumlah = pesanan[4]
            total = pesanan[5]
            nama_pembeli = pesanan[6]
            alamat = pesanan[7]
            status = pesanan[8]

            if status == "belum dikirim":
                status = Palette_Warna("Yellow", "belum dikirim")
            else:
                status = "\033[4;95;40m" + status + "\033[0m"

            print(f"\t\t   ({i}). {tanggal} -- [{no_pesanan}]\
                \n\t\t\tMasker  : {nama_masker} x {jumlah}\
                \n\t\t\tWarna   : {warna} {identify_warna(warna)}\
                \n\t\t\tHarga   : Rp{total}\
                \n\t\t\tAlamat  : {alamat}\
                \n\t\t\tPembeli : {nama_pembeli}\
                \n\t\t\t\t -- {status}\n")
            i += 1

    def update_pesanan(self):
        self.list_pesanan = [pesanan for pesanan in akun_toko[0].list_pesanan if self.nama == pesanan[6]]

# =========================================================
#                           DATA
# =========================================================

akun_toko = [
    Toko(
        nama = "Fortran",
        password = "0439"
    )
]

akun_pembeli = []

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
    else: return False

# return Boolean
def password_benar(tipe_akun, nama, password):
    for akun in tipe_akun:
        if akun.nama == nama:
            if akun.password == password:
                return True
    else: return False


# return Masker
def masker_tersedia(input):
    list_nama = [
        masker.nama.casefold() \
        for masker in akun_toko[0].list_masker
    ]
    list_warna = [
        masker.warna.casefold() \
        for masker in akun_toko[0].list_masker
    ]

    for nama_masker in list_nama:
        if input.casefold() in nama_masker \
        or input.casefold() in list_warna:
            return True
    else: return False

def masker_dipilih(input):
    masker_ditemukan = []
    for masker in akun_toko[0].list_masker:
        if input.casefold() in masker.nama.casefold() \
            or input.casefold() == masker.warna.casefold():
            masker_ditemukan.append(masker)
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
def list_ASCII(list_data):
    list_ascii = []
    for elemen in list_data:
        elemen = str(elemen)
        total = 0
        for char in elemen:
            total += ord(char)
        list_ascii.append(total)

    return list_ascii

def str_to_ASCII(string):
    list_ascii = [ord(char) for char in string]
    return list_ascii

def ASCII_to_str(list_ascii):
    string = ""
    for ascii in list_ascii:
        char = chr(ascii)
        string += char
    return string
    
def interpolation_search(list_data, data):
    list_elemen = list_data.copy()

    list_ascii = list_ASCII(list_elemen)
    insertion_sort(list_ascii)
    list_ascii_data = str_to_ASCII(data)
    data_ascii = sum(list_ascii_data)

    index = -1
    low = 0
    high = len(list_ascii)-1

    while list_ascii[low] < data_ascii \
        and list_ascii[high] > data_ascii:

        pos = (data_ascii - list_ascii[low]) // (list_ascii[high] - list_ascii[low]) * (high - low) + low

        if list_ascii[pos] < data_ascii:
            low = pos + 1
        elif list_ascii[pos] > data_ascii:
            high = pos - 1
        else:
            index = pos
            break

    if list_ascii[low] == data_ascii:
        index = low
    elif list_ascii[high] == data_ascii:
        index = high

    if index == -1:
        return None
    else:
        elemen = ASCII_to_str(list_ascii_data)
        index = list_data.index(elemen)
        return index

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
        insertion_sort(list_harga)

        list_masker = sort_berdasarkan("nama")
        list_return = []

        while len(list_return) != len(list_harga):
            for i in range(len(list_harga)):
                for masker in list_masker:
                    if list_harga[i] == masker.harga:
                        list_return.append(masker)
                        list_masker.remove(masker)

        return list_return

    elif kategori == "nama":
        list_nama = [masker.nama for masker in akun_toko[0].list_masker]        
        insertion_sort(list_nama)

        list_masker = akun_toko[0].list_masker.copy()

        list_return = []
        while len(list_return) != len(list_nama):
            for i in range(len(list_nama)):
                for masker in list_masker:
                    if list_nama[i] == masker.nama:
                        list_return.append(masker)
                        list_masker.remove(masker)

        return list_return

    elif kategori == "warna":
        list_warna = [masker.warna for masker in akun_toko[0].list_masker]        
        insertion_sort(list_warna)

        list_masker = akun_toko[0].list_masker.copy()

        list_return = []
        while len(list_return) != len(list_warna):
            for i in range(len(list_warna)):
                for masker in list_masker:
                    if list_warna[i] == masker.warna:
                        list_return.append(masker)
                        list_masker.remove(masker)

        return list_return
    
    elif kategori == "stok":
        list_stok = [masker.jumlah for masker in akun_toko[0].list_masker]
        insertion_sort(list_stok)

        list_masker = sort_berdasarkan("nama")

        list_return = []
        while len(list_return) != len(list_stok):
            for i in range(len(list_stok)):
                for masker in list_masker:
                    if list_stok[i] == masker.jumlah:
                        list_return.append(masker)
                        list_masker.remove(masker)

        return list_return



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
    ColourTupleA = (
        "Black","Red","Green",
        "Orange","Blue","Purple",
        "Cyan","White"
        )
    ColourTupleB = (
        "Grey","LRed","LGreen",
        "Yellow","LBlue","Pink",
        "LCyan"
        )
    FontTuple = (
        "Reset","Bold","Disable",
        0,"Underline",0,0,
        "Reverse","Invisible","Strikethrough"
        )

    if ColourCode in ColourTupleA:
        ColourNumber = 30 + ColourTupleA.index(ColourCode)
    elif ColourCode in ColourTupleB:
        ColourNumber = 90 + ColourTupleB.index(ColourCode)
    FontNumber = FontTuple.index(fonteu)
    return f"\033[{FontNumber};{ColourNumber}m{text}\033[0m"

def printc(ColourCode="White", text="", fonteu="Reset"):
    print(Palette_Warna(ColourCode, text, fonteu))

def inputc(ColourCode, text, fonteu):
    return input(f"{Palette_Warna(ColourCode, text, fonteu)}")

def identify_warna(warna_text='putih'):
    warna = warna_text.casefold()
    list_warna_bahasa_Indonesia =[
    'merah', 'hijau', 'abu-abu',
    'putih', 'navy', 'biru',
    'toska', 'pink', 'kuning',
    'oranye', 'orange', 'jingga'
    ]
    English_Colour_list = [
    "LRed", "Green", "Grey",
    "White", "Blue", "LBlue",
    "LCyan", "Pink", "Yellow",
    "Orange", "Orange", "Orange"
    ]

    if warna == "hitam":
        return "□"
    elif warna in list_warna_bahasa_Indonesia:
        indexNum = list_warna_bahasa_Indonesia.index(warna)
        warna_ENG =  English_Colour_list[indexNum]
        return Palette_Warna(warna_ENG, "■", "Reset")
    else:
        return ""



# UPDATE PENYIMPANAN ====================================================
# download data dari database
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

# download data dari database
def update_pembeli():
    global akun_pembeli

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    select_akun = """SELECT * FROM tabel_akun_pembeli"""
    list_akun = list(cur.execute(select_akun))
    
    akun_pembeli.clear()
    for akun in list_akun:
        nama, password = akun
        akun_pembeli.append(
            Pembeli(
                nama = nama,
                password = password
            )
        )

    con.commit()
    con.close()

# buat akun baru
def akun_pembeli_baru(nama, password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    tambah_akun = f"""INSERT INTO tabel_akun_pembeli
                    (nama, password) VALUES
                    ('{nama}', '{password}')"""

    cur.execute(tambah_akun)

    con.commit()
    con.close()

    update_pembeli()

def sinkronisasi_data():
    update_toko()
    update_pembeli()


#########################################################################
#                                ANTARMUKA
#########################################################################


# ==================================== LOGIN ====================================

#Pintu Exit
def Persetujuan_Exit(warning="                                          "):
    clear()

    print(f"""\n\n\n\n\n
\t\tO                                          O
\t\t:                                          :
\t\t:                  [---]                   :
\t\t:__________________________________________:
\t\t|'                                        '|
\t\t|      Apakah Anda yakin ingin keluar?     |
\t\t|{warning}|
\t\t|       [1] Ya            [2] Tidak        |
\t\t \________________________________________/""")

    Respon_Menu_User = input("\t\t\t\t  >> ")
    if Respon_Menu_User == "1":
        Notif_berhasil(4)
        quit()
    elif Respon_Menu_User == "2":
        Menu_User()
    else:
        Persetujuan_Exit(
            Palette_Warna(
                "LRed",
                "           Menu tidak tersedia            ",
                "Bold"
            )
        )


#Notifikasi Keberhasilan
def Notif_berhasil(path):
    clear()

    # Jalur 1: text untuk login
    if path == 1:
        lightbulb = Palette_Warna(
            "Green",
            "•••",
            "Bold"
        )
        lightbulbX = (f"                  [{lightbulb}]                   ")
        note = Palette_Warna(
            "LGreen",
            "!LOGIN ANDA BERHASIL!",
            "Bold"
        )
        noteX = (f"           {note}          ")

    # Jalur 2: text untuk log out
    elif path == 2:
        lightbulbX = (f"                  [---]                   ")
        note = Palette_Warna(
            "LGreen",
            "!Berhasil Log out!",
            "Bold"
        )
        noteX = (f"            {note}            ")

    # Jalur 3: text untuk penyusup
    elif path == 3:
        lightbulb = Palette_Warna(
            "LRed", 
            "•••", 
            "Bold"
        )
        lightbulbX = (f"                  [{lightbulb}]                   ")
        note = Palette_Warna(
            "LRed",
            "Login Penjual Gagal, Mengeluarkan Paksa",
            "Bold"
        )
        noteX = (f" {note}  ")

    # Jalur 4: text untuk keluar program
    elif path == 4:
        lightbulb = Palette_Warna(
            "Yellow",
            "•••",
            "Bold"
        )
        lightbulbX = (f"                  [{lightbulb}]                   ")
        note = Palette_Warna(
            "LRed",
            "!Menutup Program!",
            "Bold"
        )
        noteX = (f"            {note}             ")

    elif path == 5:
        lightbulb = "   "
        lightbulbX = (f"                   {lightbulb}                    ")
        note = Palette_Warna(
            "LCyan",
            "!Melakukan Pembelian!",
            "Bold"
        )
        noteX = (f"           {note}          ")

    elif path == 6:
        lightbulb = "   "
        lightbulbX = (f"                   {lightbulb}                    ")
        note = Palette_Warna(
            "LCyan",
            "!Mengedit Masker!",
            "Bold"
        )
        noteX = (f"             {note}            ")
    
    for i in range (6):
        if i == 0 or i == 3 or i == 6:
            wait = "         mohon tunggu sebentar.           "
        elif i == 1 or i == 4:
            wait = "         mohon tunggu sebentar..          "
        elif i == 2 or i == 5:
            wait = "         mohon tunggu sebentar...         "

        print(f"""\n\n\n\n\n
\t\tO                                          O
\t\t:                                          :
\t\t:{lightbulbX}:
\t\t:__________________________________________:
\t\t|'                                        '|
\t\t|{noteX}|
\t\t|{wait}|
\t\t|                                          |
\t\t \________________________________________/""")
        tclear(0.25)



akun_now = akun_toko[0]
def Login_Pembeli(warning="                                          "):
    global akun_now

    clear()
    print(f"""\n\n\n\n\n
\t\tO                                          O
\t\t:                                          :
\t\t:                  [{Palette_Warna("Green","••","Bold")}-]                   :
\t\t:__________________________________________:
\t\t|'                                        '|
\t\t|           -Pilih metode masuk-           |
\t\t|{warning}|
\t\t|  [0] Kembali   [1] Login   [2] Sign-Up   |
\t\t \________________________________________/""")

    # masukkan opsi
    Respon_menu_user = input("\n\t\t\t\t  >> ")

    # opsi tidak tersedia
    if Respon_menu_user not in ("1", "2", "0"):
        Login_Pembeli(
            Palette_Warna(
                "LRed",
                "           Opsi tidak tersedia!           ",
                "Bold"
            )
        )
        
    # kembali ke menu utama
    elif Respon_menu_user == "0":
        Menu_User()
        
    # login atau sign up
    else:
        print()
        print("\t\t\tKetik '//' untuk membatalkan.\n")

        # isi nama dan password, semoga paham :>
        form = ["Nama", "Password"]
        for i in range(len(form)):
            print(f"\t\t\t{form[i].ljust(10)}: ", end="")
            answer = input("")

            if answer == "//":
                Login_Pembeli(Palette_Warna("Cyan","           Aktivitas Dibatalkan           ","Bold"))
            else:
                form[i] = answer

        nama, password = tuple(form)

        # kalau mau login
        if Respon_menu_user == "1":
            # verif nama & pass
            if nama_sudah_ada(akun_pembeli, nama) \
                and password_benar(akun_pembeli, nama, password):

                # berhasil masuk, sekarang di akun si yg namanya diinput tadi
                akun_now = [pembeli for pembeli in akun_pembeli if pembeli.nama == nama]
                akun_now = akun_now[0]

                # masuk menu
                Notif_berhasil(1)
                Menu_untuk_Pembeli()

            else:
                Login_Pembeli(Palette_Warna("LRed","               Gagal Login!               ","Bold"))
        
        # kalau mau sign up
        elif Respon_menu_user == "2":

            #Verifikasi apakah nama sudah tersedia atau belum
            if nama_sudah_ada(akun_pembeli, nama):
                Login_Pembeli(Palette_Warna("LRed","              Gagal Sign up!              ","Bold"))

            else:
                # buat akun. masukkan ke list akun_pembeli di sistem
                akun_pembeli_baru(
                    nama = nama,
                    password = password
                )
                Login_Pembeli(Palette_Warna("LGreen","            Sign up Berhasil!!            ","Bold"))
            
gagal_masuk_toko = 0
def Login_Penjual(warning=""):
    global gagal_masuk_toko, akun_now

    clear()
    print("\n"*7)
    print(f"\t\t\t   {warning}")
    print("""
\t\t\t▓    <Konfirmasi Identitas> 
\t\t\t▓    Ketik // untuk membatalkan.
\t\t\t▓""")
    
    # login
    form = ["Nama", "Password"]
    for i in range(len(form)):
        print(f"\t\t\t▓\t\033[0;92m{form[i].ljust(10)}: \033[0m", end="")
        answer = input("")

        if answer == "//":
            Menu_User()
        else:
            form[i] = answer

    nama, password = tuple(form)

   #Verifikasi nama+pass 
    if nama_sudah_ada(akun_toko, nama) \
        and password_benar(akun_toko, nama, password):

        # berhasil masuk
        gagal_masuk_toko = 0
        akun_now = [
            penjual for penjual in akun_toko \
                if penjual.nama == nama
        ]
        akun_now = akun_now[0]
        Notif_berhasil(1)
        Menu_untuk_Penjual()

    else:
        # gagal masuk
        gagal_masuk_toko += 1

        # pengusiran paksa
        if gagal_masuk_toko == 3:
            Notif_berhasil(3)
            exit()

        Login_Penjual(
            Palette_Warna(
                "LRed",
                f"Gagal login ({gagal_masuk_toko}) dari (3)",
                "Bold"
            )
        )


# ===================================== MENU ======================================

# Menu?
def Menu_User(warning="                                          "):
    clear()

    print(f"""\n\n\n\n\n
\t\tO                                          O
\t\t:                                          :
\t\t:                  [{Palette_Warna("Green","•","Bold")}--]                   :
\t\t:__________________________________________:
\t\t|'            !Selamat Datang!            '|
\t\t|{warning}|
\t\t|      Masuk ke dalam program sebagai:     |
\t\t|    [1] Pembeli            [2] Penjual    |
\t\t \________________________________________/""")
    printc("Grey","\t\t    Ketik '//' untuk keluar dari program.",)

    Respon_Menu_User = input("\t\t\t\t  >> ")
    if Respon_Menu_User == "1":
        Login_Pembeli()
    elif Respon_Menu_User == "2":
        Login_Penjual()
    elif Respon_Menu_User == "//":
        Persetujuan_Exit()
    else:
        Menu_User(
            Palette_Warna(
                "LRed",
                "           Menu tidak tersedia            ",
                "Bold"
            )
        )

def Menu_untuk_Pembeli(warning=""):
    clear()
    nama_akun = Palette_Warna("LBlue", akun_now.nama, "Bold")
    
    print(f"""\n\n\n\n 
 

\t\t    Berikut Opsi Interaktif Kami, {nama_akun}!!
\t\t    ||   [0] Keluar
\t\t    ||   [1] Lihat daftar seluruh barang
\t\t    ||   [2] Cari nama barang
\t\t    ||   [3] Daftar pesanan
\t\t    {warning}""")

    Respon_menu_user = input("\n\t\t\t\t>> ")
    
    if Respon_menu_user == "0":
        Notif_berhasil(2)
        Menu_User()
    elif Respon_menu_user == "1":
        menu_sorting()
    elif Respon_menu_user == "2":
        menu_searching(Menu_untuk_Pembeli)
    elif Respon_menu_user == "3":
        menu_pesanan_pembeli()
    else:
        Menu_untuk_Pembeli(
            Palette_Warna(
            "LRed",
            "Opsi tidak tersedia!", 
            "Bold"
            )
        )

def Menu_untuk_Penjual(warning=""):
    clear()
    nama_akun = Palette_Warna("LBlue", akun_now.nama, "Bold")
    print(f"""\n\n\n\n 
    

\t\t    Berikut Opsi Interaktif Kami, {nama_akun}!!
\t\t    ||   [0] Keluar
\t\t    ||   [1] Lihat daftar seluruh masker
\t\t    ||   [2] Cari masker
\t\t    ||   [3] Tambah Masker Jenis Baru
\t\t    ||   [4] Daftar pesanan masuk
\t\t    {warning}"""
    )

    Respon_menu_user = input("\n\t\t\t\t>> ")

    if Respon_menu_user == "0":
        Notif_berhasil(2)
        Menu_User()
    elif Respon_menu_user == "1":
        menu_sorting()
    elif Respon_menu_user == "2":
        menu_searching(Menu_untuk_Penjual)
    elif Respon_menu_user == "3":
        menu_tambah_masker()
    elif Respon_menu_user == "4":
        menu_pesanan_penjual()
    else:
        Menu_untuk_Penjual(
            Palette_Warna(
                "LRed",
                "Opsi tidak tersedia!", 
                "Bold"
            )
        )


# = = = = = = = = = = = = = = = = = MENU YANG SAMA = = = = = = = = = = = = = = = = = = 

# sorting masker + beli masker (pembeli) v edit masker (penjual)
def menu_sorting(warning=""):
    clear()

    print(f"""\n\n\n\n 
    

\t\t    Pilih metode pengurutan barang:
\t\t    ||   [0] Kembali
\t\t    ||   [1] Berdasarkan Nama
\t\t    ||   [2] Berdasarkan Warna
\t\t    ||   [3] Berdasarkan Ketersediaan / Stok
\t\t    ||   [4] Berdasarkan Harga Terendah
\t\t    ||   [5] Berdasarkan Harga Tertinggi
\t\t    {warning}""")
    kategori = input("\n\t\t\t>> ")

    # kondisi
    list_masker = None
    indikator = None

    # kembali ke menu
    if kategori == "0":
        if type(akun_now) == Pembeli:
            Menu_untuk_Pembeli()
        else:
            Menu_untuk_Penjual()

    elif kategori == "1":
        indikator = "nama"
        list_masker = sort_berdasarkan(indikator)
    elif kategori == "2":
        indikator = "warna"
        list_masker = sort_berdasarkan(indikator)
    elif kategori == "3":
        indikator = "stok"
        list_masker = sort_berdasarkan(indikator)
    elif kategori == "4":
        indikator = "harga (ascending)"
        list_masker = sort_berdasarkan("harga")
    elif kategori == "5":
        indikator = "harga (descending)"
        list_masker = sort_berdasarkan("harga")
        list_masker = [
            list_masker[i] \
            for i in range(len(list_masker)-1, -1, -1)
        ]

    # warning
    else:
        menu_sorting(
            Palette_Warna(
                "LRed",
                "Opsi tidak tersedia!", 
                "Bold"
            )
        )

    tampilkan_daftar_masker(
        subjudul = f"Sort berdasarkan {indikator}.",
        list_masker = list_masker
    )

# search masker
def menu_searching(menu_back, warning=""):
    clear()
    print(f"\n\n\n\n\n\n\t{warning}")
    printc("Grey","\t\t\t _____________________",)
    Barang_dituju = input("\n\t\t\t▒\033[4;37m Cari masker: ")
    printc("White","","Bold")

    # masker yg dicari ada
    masker_ditemukan = masker_dipilih(Barang_dituju)
    if masker_tersedia(Barang_dituju) \
        and not Barang_dituju.isspace() \
        and Barang_dituju != "":

        # tampilkan masker
        tampilkan_daftar_masker(
            subjudul = f"Hasil pencarian '{Barang_dituju}':",
            list_masker = masker_ditemukan
        )

    # masker yg dicari tidak ada
    else:

        #timed cls 1s
        for i in range(2,0,-1):
            clear()
            print(f"\n\n\n\n\n\n\t{warning}")
            printc("Grey","\t\t\t _____________________",)
            print(f"\n\t\t\t▒\033[4;37m Cari masker: {Barang_dituju}")
            printc("White","","Bold")

            printc("Grey","\n\n\t\t\t▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒","Bold")
            print(          
                f"\n\n\t\t\t|   Barang tidak ditemukan    |\
                    \n\t\t\t|          atau               |\
                    \n\t\t\t| sedang tidak tersedia ({i}s)  |")
            printc("Grey","\n\n\t\t\t▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒","Bold")

            tclear(1)
        menu_back(Palette_Warna("LRed", "Masker tidak ditemukan!", "Bold"))

# tampilan daftar masker
def tampilkan_daftar_masker(subjudul, list_masker, warning=""):
    clear()

    printc("White","\n\n\t\t\tDaftar Masker", "Bold")
    print("\t\t\t========================")
    print(f"\t\t\t{subjudul}\n")

    # tampilkan daftar masker
    print(("\t\t" + "█"*50))

    i = 1
    for masker in list_masker:
        print("\t"*4+f"     ---- {i} ----")
        masker.tampilkan_data()
        print()
        print("\t\t"+"█"*50)
        i += 1

    # di akun pembeli --> tanyakan apakah ingin beli
    if type(akun_now) == Pembeli:
        transaksi_pesanan(
            subjudul, 
            list_masker,
            warning
        )

    # di akun penjual --> tanyakan apakah ingin manipulasi masker
    else:
        pilih_masker(
            subjudul,
            list_masker,
            warning
        )
    

# = = = = = = = = = = = = = = = = = = MENU.PEMBELI = = = = = = = = = = = = = = = = = = = 

# daftar pesanan pembeli
def menu_pesanan_pembeli():
    clear()

    # judul halaman
    print("\n\n\n\n\n\t\t\t\tDaftar Pesanan Anda")
    print("\t\t\t\t===================\n")

    # jika belum pesan apa-apa
    if len(akun_now.list_pesanan) == 0:
        printc("Yellow","\t\t\t\tAnda belum membeli barang.",)
        
        input("\n\n\t\t\t\t\tKembali => ")
        Menu_untuk_Pembeli()
    # jika sudah pesan
    else:
        akun_now.tampilkan_pesanan()
        
        input("\n\n\t\t\tKembali =>")
        Menu_untuk_Pembeli()

# tanyakan apakah melakukan transaksi
def transaksi_pesanan(subjudul, list_masker, warning=""):
    # pilihan setelah melihat daftar masker
    print(
        f"\n\t\t\t[1] Pesan masker\
        \n\t\t\t[2] Kembali\
        \n\t\t\t{warning}"
    )
    respon = input("\t\t\t>> ")

    # jika pesan masker
    if respon == "1":
        kode_masker = input("\n\t\t\tKode masker\t: ")

        # cek kode ada atau tidak
        index_masker = interpolation_search(
            list_data = [
                masker.kode \
                for masker in akun_toko[0].list_masker
            ],
            data = kode_masker
        )

        # jika masker ada
        if index_masker is not None:
            print() 

            masker = akun_toko[0].list_masker[index_masker]

            form = ["Jumlah barang", "Alamat Anda"]
            for i in range(len(form)):
                answer = input(f"\t\t\t{form[i].ljust(15)}\t : ")

                # jumlah yg dimasukkan
                if i == 0:
                    try:
                        answer = int(answer)
                        if jumlah_masuk_akal(answer) \
                            and answer <= masker.jumlah:
                            pass
                        else:
                            tampilkan_daftar_masker(
                                subjudul,
                                list_masker,
                                warning = Palette_Warna(
                                    "LRed",
                                    "Stok tidak mencukupi!",
                                    "Bold"
                                )
                            )
                    except ValueError:
                        tampilkan_daftar_masker(
                            subjudul,
                            list_masker,
                            warning = Palette_Warna(
                                "LRed",
                                "Jumlah tidak valid!",
                                "Bold"
                            )
                        )

                form[i] = answer

                """ PROSES PEMBELIAN
                akun_now = akun yg login
                akun_toko[0]        = akun toko ini
                form[0]             = jumlah barang
                form[1]             = alamat barang
                """

            printc(
                "Yellow",
                f"\n\t\t\tTotal yang harus dibayar adalah Rp{form[0]*masker.harga}",
                "Bold"
            )
            respon = input(
                "\033[1;33m\t\t\tKetik '1' untuk melanjutkan pembelian\n\t\t\t\t\t>>\033[0m "
            )
        
            if respon == "1":
                # pesanan diproses
                akun_now.pesan_masker(
                    akun_toko[0], 
                    kode_masker, 
                    form[0], 
                    form[1]
                )
                Notif_berhasil(5)
                Menu_untuk_Pembeli(
                    warning = Palette_Warna(
                        "LGreen",
                        "Pembelian berhasil!",
                        "Bold"
                    )
                )

            else:
                # pesanan batal
                tampilkan_daftar_masker(
                    subjudul,
                    list_masker,
                    warning = Palette_Warna(
                        "LRed",
                        "Pembelian dibatalkan.",
                        "Bold"
                    )
                )
                
        # jika tidak ada
        else:
            tampilkan_daftar_masker(
                subjudul,
                list_masker,
                warning= Palette_Warna(
                    "LRed",
                    "Masker tidak ditemukan!",
                    "Bold"
                )
            )

    # jika tidak pesan masker
    elif respon == "2":
        Menu_untuk_Pembeli()

    # jika opsi tidak tersedia
    else:
        tampilkan_daftar_masker(
            subjudul,
            list_masker,
            warning = Palette_Warna(
                "LRed",
                "Opsi tidak tersedia!",
                "Bold"
            )
        )


# = = = = = = = = = = = = = = = = = = MENU.PENJUAL = = = = = = = = = = = = = = = = = = = 

def menu_tambah_masker(warning=""):
    clear()
    print("""\n\n\n\n 
    


\t\t    ▓ Tambahkan Masker Baru""")
    print(f"\t\t    |\n\t\t    ▓ {warning}\n\t\t    |")
    print("\t\t    ▓ Ketik '//' untuk membatalkan aktivitas\n\t\t    |")

    form = ["Nama masker", "Warna", "Harga", "Jumlah"]
    for i in range(len(form)):
        answer = input(f"\t\t    ▓ {form[i].ljust(15)}: ")

        if answer == "//":
            Menu_untuk_Penjual(
                Palette_Warna(
                    "Cyan",
                    "Aktivitas dibatalkan.",
                    "Bold"
                )
            )
        elif form[i] in (form[2], form[3]):
            try:
                answer = int(answer)
            except ValueError:
                menu_tambah_masker(
                    warning = Palette_Warna(
                        "LRed",
                        f"{form[i]} tidak valid!",
                        "Bold"
                    )
                )
        form[i] = answer
        
    akun_now.tambah_masker_baru(
            nama_masker = form[0],
            warna = form[1],
            harga = form[2],
            jumlah = form[3],
            kode = kode_masker(
            num = len(akun_now.list_masker)-1, 
            warna = form[1]
        )
    )

    Menu_untuk_Penjual(
        Palette_Warna(
            "LGreen",
            "Berhasil menambahkan masker!",
            "Bold"
        )
    )
    

# daftar pesanan masuk + kirim barang
def menu_pesanan_penjual(warning=""):
    clear()

    # judul halaman
    print("\n\n\n\n\n\t\t\t\tDaftar Pesanan Masuk")
    print("\t\t\t\t====================\n")

    # jika daftar pesanan masih kosong
    if len(akun_now.list_pesanan) == 0:
        printc("Yellow", "\t\t\t\tBelum ada pesanan masuk.")
        input("\n\n\t\t\t\t\tKembali => ")
        Menu_untuk_Penjual()

    # jika daftar pesanan sudah terisi
    else:
        akun_now.tampilkan_pesanan()
        print(f"\n\t\t\t{warning}")
        respon = input("\n\t\t\tKetik '1' untuk mengirim masker\n\t\t\t>> ")

        # jika benar-benar membeli
        if respon == "1":
            no_pesanan = input("\n\t\t\tNomor pesanan\t: ")
            list_no_pesanan = [
                pesanan[1] \
                for pesanan in akun_now.list_pesanan
            ]

            if no_pesanan in list_no_pesanan:
                index = list_no_pesanan.index(no_pesanan)

                if akun_now.list_pesanan[index][7] == "sudah dikirim":
                    menu_pesanan_penjual(
                        warning = Palette_Warna(
                            "LRed",
                            "Pesanan telah dikirim sebelumnya!",
                            "Bold"
                        )
                    )
                else:
                    akun_now.kirim_masker(
                        no_pesanan = no_pesanan
                    )
                    printc(
                        "LGreen",
                        f"\n\t\t\tPesanan {no_pesanan} telah berhasil dikirim!"
                    )
            else:
                menu_pesanan_penjual(
                    warning = Palette_Warna(
                        "LRed",
                        "Nomor pesanan tidak ditemukan!",
                        "Bold"
                    )
                )

        input("\n\n\t\t\t\t\tKembali =>")
        Menu_untuk_Penjual()

# masker yang mau diedit
def pilih_masker(subjudul, list_masker, warning=""):
    # menu yang tersedia
    print(
        f"\n\t\t\t[1] Ubah masker\
        \n\t\t\t[2] Kembali\
        \n\t\t\t{warning}"
    )
    respon = input("\n\t\t\t>> ")
    
    # ubah masker
    if respon == "1":
        kode_masker = input("\n\t\t\tKode masker : ")
        clear()

        # cek masker
        index_masker = interpolation_search(
            list_data = [
                masker.kode \
                for masker in akun_toko[0].list_masker
            ],
            data = kode_masker
        )

        # edit masker yg dicari
        if index_masker is not None:
            edit_masker(akun_toko[0].list_masker[index_masker])

            # jika batal edit masker
            tampilkan_daftar_masker(
                subjudul,
                list_masker
            )

        # masker yg dicari tidak ada
        else:
            tampilkan_daftar_masker(
                subjudul,
                list_masker,
                warning = Palette_Warna(
                    "LRed",
                    "Masker tidak ditemukan.",
                    "Bold"
                )
            )

    # kembali
    elif respon == "2":
        Menu_untuk_Penjual()

    # opsi tidak tersedia
    else:
        tampilkan_daftar_masker(
            subjudul, 
            list_masker,
            warning = Palette_Warna(
                "LRed", 
                "Opsi tidak tersedia!", 
                "Bold"
            )
        )

# menu manipulasi stok masker
def edit_masker(masker, warning=""):
    clear()

    print("\n\n\n\n\n\n\t\t"+"██████████████████████████████"*2)
    masker.tampilkan_data()
    print("\t\t"+"██████████████████████████████"*2)

    print(f"""\n
\t\t\tBerikut opsi edit yang tersedia:
\t\t\t||   [1] Tambah stok masker
\t\t\t||   [2] Kurangi stok masker
\t\t\t||   [3] Hapus masker
\t\t\t||   [4] Kembali
\t\t\t{warning}""")

    Respon_menu_user = input("\n\t\t\t>> ")
    print()

    # tambah stok
    if Respon_menu_user == "1":
        try:
            jumlah = int(input("\t\t\tJumlah\t: "))

            if jumlah_masuk_akal(jumlah):
                akun_now.restok_masker(
                    mode = "tambah",
                    kode = masker.kode,
                    jumlah = jumlah
                )

            else:
                edit_masker(
                    masker, 
                    warning = Palette_Warna(
                        "LRed",
                        "Jumlah tidak valid!",
                        "Bold"
                    )
                )

        except ValueError:
            edit_masker(
                masker, 
                warning = Palette_Warna(
                    "LRed",
                    "Jumlah tidak valid!",
                    "Bold"
                )
            )
        
        Notif_berhasil(6)
        Menu_untuk_Penjual(
            warning = Palette_Warna(
            "LGreen",
            "Stok masker berhasil ditambahkan!",
            "Bold"))
    # kurangi stok
    elif Respon_menu_user == "2":
        try:
            jumlah = int(input("\t\t\tJumlah\t: "))

            if jumlah_masuk_akal(jumlah):
                akun_now.restok_masker(
                    mode = "kurang",
                    kode = masker.kode,
                    jumlah = jumlah
                )

            else:
                edit_masker(
                    masker, 
                    warning = Palette_Warna(
                        "LRed",
                        "Jumlah tidak valid!",
                        "Bold"
                    )
                )
            
        except ValueError:
            edit_masker(
                masker, 
                warning = Palette_Warna(
                    "LRed",
                    "Jumlah tidak valid!",
                    "Bold"
                )
            )
        
        Notif_berhasil(6)
        Menu_untuk_Penjual(
            warning = Palette_Warna(
            "LGreen",
            "Stok masker berhasil dikurangi!",
            "Bold"))
    
    # hapus masker
    elif Respon_menu_user == "3":

        for mask in akun_now.list_masker:
            if mask == masker:
                akun_now.hapus_masker(masker.kode)

        Notif_berhasil(6)
        Menu_untuk_Penjual(
            warning = Palette_Warna(
                "LGreen",
                "Masker berhasil dihapus.",
                "Bold"
            )
        )

    # kembali ke menu            
    elif Respon_menu_user == "4":
        pass

    # opsi tidak tersedia
    else:
        edit_masker(
            masker, 
            warning=Palette_Warna(
                "LRed",
                "Opsi tidak tersedia!",
                "Bold"
            )
        )

    Menu_untuk_Penjual()

if __name__ == "__main__":
    while True:
        sinkronisasi_data()
        Menu_User()

