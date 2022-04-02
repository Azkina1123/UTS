from tkinter.font import BOLD
from sistem import *

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
                        f"\n\t\t\t\
                            Pesanan {no_pesanan} telah berhasil dikirim!"
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

# ==================================== START ====================================

if __name__ == "__main__":
    while True:
        sinkronisasi_data()
        Menu_User()