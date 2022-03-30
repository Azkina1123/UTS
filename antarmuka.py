from tkinter.font import BOLD
from sistem import *

# ==================================== LOGIN ====================================

#Notifikasi Keberhasilan
def Notif_berhasil(path):
    clear()

    # Jalur 1: text untuk login
    if path == 1:
        lightbulb = Palette_Warna("Green","•••","Bold")
        lightbulbX = (f"                  [{lightbulb}]                   ")
        note = Palette_Warna("LGreen","!LOGIN ANDA BERHASIL!","Bold")
        noteX = (f"           {note}          ")

    # Jalur 2: text untuk log out
    elif path == 2:
        lightbulbX = (f"                  [---]                   ")
        note = Palette_Warna("LGreen","!Berhasil Log out!","Bold")
        noteX = (f"            {note}            ")

    elif path == 3:
        lightbulb = Palette_Warna("LRed","•••","Bold")
        lightbulbX = (f"                  [{lightbulb}]                   ")
        note = Palette_Warna("LRed","Login Penjual Gagal, Mengeluarkan Paksa","Bold")
        noteX = (f" {note}  ")
    


    print(f"""\n\n\n\n\n
\t\tO                                          O
\t\t:                                          :
\t\t:{lightbulbX}:
\t\t:__________________________________________:
\t\t|'                                        '|
\t\t|{noteX}|
\t\t|         mohon tunggu sebentar...         |
\t\t|                                          |
\t\t \________________________________________/""")
    tclear(2)


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
\t\t|  [1] Login   [2] Sign-up   [3] Kembali   |
\t\t \________________________________________/""")

    # masukkan opsi
    Respon_menu_user = input("\n\t\t\t\t  >> ")

    # opsi tidak tersedia
    if Respon_menu_user not in ("1", "2", "3"):
        Login_Pembeli(Palette_Warna("LRed","           Opsi tidak tersedia!           ","Bold"))
        
    # kembali ke menu utama
    elif Respon_menu_user == "3":
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
                akun_pembali_baru(
                    nama = nama,
                    password = password
                )
                Login_Pembeli(Palette_Warna("LGreen","            Sign up Berhasil!!            ","Bold"))
            
gagal_masuk_toko = 0
def Login_Penjual(warning=""):
    global gagal_masuk_toko, akun_now

    clear()
    print("\n"*5)
    print(f"\t\t   {warning}")
    print("""
\t\t▓    <Konfirmasi Identitas> 
\t\t▓    Ketik // untuk membatalkan.
\t\t▓""")
    
    # login
    form = ["Nama", "Password"]
    for i in range(len(form)):
        print(f"\t\t▓\t\033[0;92;40m{form[i].ljust(10)}: \033[0m", end="")
        answer = input("")

        if answer == "//":
            Menu_User()
        else:
            form[i] = answer

    nama, password = tuple(form)

   #Verifikasi nama+pass 
    if nama_sudah_ada(akun_toko, nama) and password_benar(akun_toko, nama, password):

        # berhasil masuk
        gagal_masuk_toko = 0
        akun_now = [penjual for penjual in akun_toko if penjual.nama == nama]
        akun_now = akun_now[0]
        Menu_untuk_Penjual()

    else:
        # gagal masuk
        gagal_masuk_toko += 1

        # pengusiran paksa
        if gagal_masuk_toko == 3:
            Notif_berhasil(3)
            exit()

        Login_Penjual(Palette_Warna("LRed",f"Gagal login ({gagal_masuk_toko}) dari (3)","Bold"))


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


    Respon_Menu_User = input("\n\t\t\t\t  >> ")
    if Respon_Menu_User == "1":
        Login_Pembeli()
    elif Respon_Menu_User == "2":
        #cls
        Login_Penjual()
    else:
        Menu_User(Palette_Warna("LRed","           Menu tidak tersedia            ","Bold"))

def Menu_untuk_Pembeli(warning=""):
    clear()
    print(f""" 
 

    Berikut Opsi Interaktif Kami, {akun_now.nama}!!
    ||   [1] Lihat daftar seluruh barang
    ||   [2] Cari nama barang
    ||   [3] Daftar pesanan
    ||   [4] Keluar
    {warning}""")
    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    Respon_menu_user = input("\n\t\t>> ")
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

    if Respon_menu_user == "1":
        menu_sorting()
    elif Respon_menu_user == "2":
        menu_searching(Menu_untuk_Pembeli)
    elif Respon_menu_user == "3":
        menu_pesanan_pembeli()
    elif Respon_menu_user == "4":
        Notif_berhasil(2)
        Menu_User()
    else:
        Menu_untuk_Pembeli(Palette_Warna("LRed","Opsi tidak tersedia!", "Bold"))

def Menu_untuk_Penjual(warning=""):
    clear()

    print(f""" 
    


    Berikut Opsi Interaktif Kami, {akun_now.nama}!!
    ||   [1] Lihat daftar seluruh masker 
    ||   [2] Cari masker
    ||   [3] Tambah Masker Jenis Baru
    ||   [4] Daftar pesanan masuk
    ||   [5] Keluar
    {warning}"""
    )

    Respon_menu_user = input("\n\t\t>> ")

    if Respon_menu_user == "1":
        menu_sorting()
    elif Respon_menu_user == "2":
        menu_searching(Menu_untuk_Penjual)
    elif Respon_menu_user == "3":
        menu_tambah_masker()
    elif Respon_menu_user == "4":
        menu_pesanan_penjual()
    elif Respon_menu_user == "5":
        Notif_berhasil(2)
        Menu_User()
    else:
        Menu_untuk_Pembeli(Palette_Warna("LRed","Opsi tidak tersedia!", "Bold"))


# = = = = = = = = = = = = = = = = = MENU YANG SAMA = = = = = = = = = = = = = = = = = = 

# sorting masker + beli masker (pembeli) v edit masker (penjual)
def menu_sorting(warning=""):
    clear()

    print(f""" 
    

    Pilih metode pengurutan barang:
    ||   [1] Berdasarkan Nama
    ||   [2] Berdasarkan Warna
    ||   [3] Berdasarkan Ketersediaan / Stok
    ||   [4] Berdasarkan Harga Terendah
    ||   [5] Berdasarkan Harga Tertinggi
    ||   [6] Kembali
    {warning}""")
    kategori = input("\n\t>> ")

    # kondisi
    list_masker = None
    indikator = None
    if kategori == "1":
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
        list_masker = [list_masker[i] for i in range(len(list_masker)-1, -1, -1)]

    # kembali ke menu
    elif kategori == "6":
        if type(akun_now) == Pembeli:
            Menu_untuk_Pembeli()
        else:
            Menu_untuk_Penjual()
    # warning
    else:
        menu_sorting(Palette_Warna("LRed","Opsi tidak tersedia!", "Bold"))

    tampilkan_daftar_masker(
        subjudul = f"Sort berdasarkan {indikator}.",
        list_masker = list_masker
    )

# search masker
def menu_searching(menu_back, warning=""):
    clear()
    print(f"\t{warning}")
    printc("Grey","\t\t\t _____________________",)
    Barang_dituju = input("\n\t\t\t▒\033[4;37;40m Cari masker: ")
    printc("White","","Bold")

    # masker yg dicari ada
    if masker_tersedia(Barang_dituju):

        # tampilkan masker
        masker_ditemukan = masker_dipilih(Barang_dituju)
        tampilkan_daftar_masker(
            subjudul = f"Hasil pencarian '{Barang_dituju}':",
            list_masker = masker_ditemukan
        )

    # masker yg dicari tidak ada
    else:

        #timed cls 1s
        for i in range(3,0,-1):
            print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")
        menu_back("Masker tidak ditemukan!")

# tampilan daftar masker
def tampilkan_daftar_masker(subjudul, list_masker, warning=""):
    clear()

    printc("White","\n\tDaftar Masker", "Bold")
    print("\t========================")
    print(f"\t{subjudul}\n")

    # tampilkan daftar masker
    print(("█"*50).center(30))
    i = 1
    for masker in list_masker:
        print(f"---- {i} ----".center(30))
        masker.tampilkan_data()
        print()
        print(("█"*50).center(30))
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
    print("\n\n\tDaftar Pesanan Anda")
    print("\t===================\n")

    # jika belum pesan apa-apa
    if len(akun_now.list_pesanan) == 0:
        printc("Yellow","\tAnda belum membeli barang.",)
        
        input("\n\n\t\tKembali => ")
        Menu_untuk_Pembeli()
    # jika sudah pesan
    else:
        akun_now.tampilkan_pesanan()
        
        input("\n\n\t\tKembali =>")
        Menu_untuk_Pembeli()

# tanyakan apakah melakukan transaksi
def transaksi_pesanan(subjudul, list_masker, warning=""):
    # pilihan setelah melihat daftar masker
    print(
        f"\n\t[1] Pesan masker\
        \n\t[2] Kembali\
        \n\t{warning}"
    )
    respon = input("\t>> ")

    # jika pesan masker
    if respon == "1":
        kode_masker = input("\n\tKode masker\t: ")

        # cek kode ada atau tidak
        index_masker = interpolation_search(
            list_data = [masker.kode for masker in akun_toko[0].list_masker],
            data = kode_masker
        )

        # jika masker ada
        if index_masker is not None:
            print() 

            masker = akun_toko[0].list_masker[index_masker]

            form = ["Jumlah barang", "Alamat Anda"]
            for i in range(len(form)):
                answer = input(f"\t{form[i].ljust(15)} : ")

                # jumlah yg dimasukkan
                if i == 0:
                    try:
                        answer = int(answer)
                        if jumlah_masuk_akal(answer) and answer <= masker.jumlah:
                            pass
                        else:
                            tampilkan_daftar_masker(
                                subjudul,
                                list_masker,
                                warning = Palette_Warna("LRed","Stok tidak mencukupi!","Bold")
                            )
                    except ValueError:
                        tampilkan_daftar_masker(
                            subjudul,
                            list_masker,
                            warning = Palette_Warna("LRed","Jumlah tidak valid!","Bold")
                        )

                form[i] = answer

                """ PROSES PEMBELIAN
                akun_now = akun yg login
                akun_toko[0]        = akun toko ini
                form[0]             = jumlah barang
                form[1]             = alamat barang
                """

            print(f"\tTotal yang harus dibayar adalah Rp{form[0]*masker.harga}")
            respon = input("\n\tKetik '1' untuk melanjutkan pembelian\n\t>> ")
        
            if respon == "1":
                # pesanan diproses
                akun_now.pesan_masker(akun_toko[0], kode_masker, form[0], form[1])
                Menu_untuk_Pembeli(warning="Pembelian berhasil!")

            else:
                # pesanan batal
                tampilkan_daftar_masker(
                    subjudul,
                    list_masker,
                    warning="Pembelian dibatalkan."
                )
                
        # jika tidak ada
        else:
            tampilkan_daftar_masker(
                subjudul,
                list_masker,
                warning= Palette_Warna("LRed","Masker tidak ditemukan!","Bold")
            )

    # jika tidak pesan masker
    elif respon == "2":
        input("\n\t\tKembali => ")
        Menu_untuk_Pembeli()

    # jika opsi tidak tersedia
    else:
        tampilkan_daftar_masker(
            subjudul,
            list_masker,
            warning= Palette_Warna("LRed","Opsi tidak tersedia!","Bold")
        )


# = = = = = = = = = = = = = = = = = = MENU.PENJUAL = = = = = = = = = = = = = = = = = = = 

def menu_tambah_masker(warning=""):
    clear()
    print("\tTambahkan Masker Baru")
    print(f"\t\n{warning}\n")
    print("Ketik '//' untuk membatalkan aktivitas\n")

    form = ["Nama masker", "Warna", "Harga", "Jumlah"]
    for i in range(len(form)):
        answer = input(f"\t{form[i].ljust(15)}: ")

        if answer == "//":
            Menu_untuk_Penjual(Palette_Warna("Cyan","Aktivitas dibatalkan.","Bold"))
        elif form[i] in (form[2], form[3]):
            try:
                answer = int(answer)
            except ValueError:
                menu_tambah_masker(warning=Palette_Warna("LRed",f"{form[i]} tidak valid!","Bold"))
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

    Menu_untuk_Penjual(Palette_Warna("LGreen","Berhasil menambahkan masker!","Bold"))
    

# daftar pesanan masuk + kirim barang
def menu_pesanan_penjual(warning=""):
    clear()

    # judul halaman
    print("\n\n\tDaftar Pesanan Masuk")
    print("\t===================\n")
    print(f"{warning}")

    # jika daftar pesanan masih kosong
    if len(akun_now.list_pesanan) == 0:
        print("\tBelum ada pesanan masuk.")
        input("\n\n\t\tKembali => ")
        Menu_untuk_Penjual()

    # jika daftar pesanan sudah terisi
    else:
        akun_now.tampilkan_pesanan()

        respon = input("\n\nKetik '1' untuk mengirim masker\n\t>> ")

        # jika benar-benar membeli
        if respon == "1":
            no_pesanan = input("Nomor pesanan\t:")

            list_no_pesanan = [pesanan[1] for pesanan in akun_now.list_pesanan]

            if no_pesanan in list_no_pesanan:
                index = list_no_pesanan.index(no_pesanan)
                if akun_now.list_pesanan[index][7] == Palette_Warna("Cyan","sudah dikirim","Bold"):
                    menu_pesanan_penjual(warning=Palette_Warna("LRed","Pesanan telah dikirim sebelumnya!","Bold"))
                else:
                    akun_now.kirim_masker(
                        no_pesanan = no_pesanan
                    )
                    printc("LGreen",f"\nPesanan {no_pesanan} telah berhasil dikirim!",)
            else:
                menu_pesanan_penjual(warning=Palette_Warna("LRed","Nomor pesanan tidak ditemukan!","Bold"))

        input("\n\n\t\tKembali =>")
        Menu_untuk_Penjual()

# masker yang mau diedit
def pilih_masker(subjudul, list_masker, warning=""):
    # menu yang tersedia
    print(
        f"\n\t[1] Ubah masker\
        \n\t[2] Kembali\
        \n\t{warning}"
    )
    respon = input("\n\t>> ")
    
    # ubah masker
    if respon == "1":
        kode_masker = input("Kode masker : ")
        clear()

        # cek masker
        index_masker = interpolation_search(
            list_data = [masker.kode for masker in akun_toko[0].list_masker],
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
                warning = Palette_Warna("LRed","Masker tidak ditemukan.","Bold")
            )

    # kembali
    elif respon == "2":
        Menu_untuk_Penjual()

    # opsi tidak tersedia
    else:
        tampilkan_daftar_masker(
            subjudul, 
            list_masker,
            warning = Palette_Warna("LRed","Opsi tidak tersedia!","Bold")
        )

# menu manipulasi stok masker
def edit_masker(masker, warning=""):
    clear()

    print("\n\n")
    masker.tampilkan_data()

    print(f""" 

    {warning}
    
    [1] Tambah stok masker
    [2] Kurangi stok masker
    [3] Hapus masker
    [4] Kembali """)

    Respon_menu_user = input("\n\t\t>> ")
    print()

    # tambah stok
    if Respon_menu_user == "1":
        try:
            jumlah = int(input("Jumlah\t: "))

            if jumlah_masuk_akal(jumlah):
                print(masker.kode)
                input()
                akun_now.restok_masker(
                    mode = "tambah",
                    kode = masker.kode,
                    jumlah = jumlah
                )

            else:
                edit_masker(
                    masker, 
                    warning=Palette_Warna("LRed","Jumlah tidak valid!","Bold")
                )

        except ValueError:
            edit_masker(
                masker, 
                warning=Palette_Warna("LRed","Jumlah tidak valid!","Bold")
            )
        
    # kurangi stok
    elif Respon_menu_user == "2":
        try:
            jumlah = int(input("Jumlah\t: "))

            if jumlah_masuk_akal(jumlah):
                akun_now.restok_masker(
                    mode = "kurang",
                    kode = masker.kode,
                    jumlah = jumlah
                )

            else:
                edit_masker(
                    masker, 
                    warning = Palette_Warna("LRed","Jumlah tidak valid!","Bold")
                )
            
        except ValueError:
            edit_masker(
                masker, 
                warning = Palette_Warna("LRed","Jumlah tidak valid!","Bold")
            )
    
    # hapus masker
    elif Respon_menu_user == "3":

        for mask in akun_now.list_masker:
            if mask == masker:
                akun_now.hapus_masker(masker.kode)

    # kembali ke menu            
    elif Respon_menu_user == "4":
        pass

    # opsi tidak tersedia
    else:
        edit_masker(
            masker, 
            warning=Palette_Warna("LRed","Opsi tidak tersedia!","Bold")
        )

    Menu_untuk_Penjual()

# ==================================== START ====================================

if __name__ == "__main__":
    while True:
        sinkronisasi_data()
        Menu_User()