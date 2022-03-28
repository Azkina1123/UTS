from logging import warning
from sistem import *

# ==================================== LOGIN ====================================

#Notifikasi Keberhasilan
def Notif_berhasil_login():
    print(f"""\n\n\n\n\n
O                                          O
:                                          :
:                  [{Palette_Warna("Green","•••","Bold")}]                   :
:__________________________________________:
|'                                        '|
|           {Palette_Warna("LGreen","!LOGIN ANDA BERHASIL!","Bold")}          |
|         mohon tunggu sebentar...         |
|                                          |
 \________________________________________/""")
    tclear(2)

akun_now = akun_toko[0]
def Login_Pembeli(warning="                                          "):
    global akun_now

    clear()
    print(f"""\n\n\n\n\n
O                                          O
:                                          :
:                  [{Palette_Warna("Green","••","Bold")}-]                   :
:__________________________________________:
|'                                        '|
|           -Pilih metode masuk-           |
|{warning}|
|  [1] Login   [2] Sign-up   [3] Kembali   |
 \________________________________________/""")

    # masukkan opsi
    Respon_menu_user = input("\n\t\t  >> ")

    # opsi tidak tersedia
    if Respon_menu_user not in ("1", "2", "3"):
        Login_Pembeli(Palette_Warna("LRed","           Opsi tidak tersedia!           ","Bold"))
        
    # kembali ke menu utama
    elif Respon_menu_user == "3":
        Menu_User()
        
    # login atau sign up
    else:
        print()
        print("\tKetik '//' untuk membatalkan.\n")

        # isi nama dan password, semoga paham :>
        form = ["Nama", "Password"]
        for i in range(len(form)):
            print(f"\t{form[i].ljust(10)}: ", end="")
            answer = input("")

            if answer == "//":
                Login_Pembeli(Palette_Warna("Cyan","           Aktivitas Dibatalkan           ","Bold"))
            else:
                form[i] = answer

        nama, password = tuple(form)

        # kalau mau login
        if Respon_menu_user == "1":
            #Verifikasi nama+pass / pembatalan pilihan --> 
            if nama_sudah_ada(akun_pembeli, nama) and password_benar(akun_pembeli, nama, password):

                # berhasil masuk, sekarang di akun si yg namanya diinput tadi
                akun_now = [pembeli for pembeli in akun_pembeli if pembeli.nama == nama]
                akun_now = akun_now[0]

                # masuk menu
                Notif_berhasil_login()
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
                akun_baru = Pembeli(nama, password)
                akun_pembeli.append(akun_baru)
                Login_Pembeli(Palette_Warna("LGreen","            Sign up Berhasil!!            ","Bold"))
            
gagal_masuk_toko = 0
def Login_Penjual(warning=""):
    global gagal_masuk_toko, akun_now

    clear()
    print("\n\n\n\n\n")
    print(warning.center(30))
    print("""
    <Konfirmasi Identitas> 
    Ketik // untuk membatalkan.\n""")
    
    # login
    form = ["Nama", "Password"]
    for i in range(len(form)):
        print(f"\t{form[i].ljust(10)}: ", end="")
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
            exit()

        Login_Penjual(f"Gagal login ({gagal_masuk_toko})")


# ===================================== MENU ======================================

# Menu?
def Menu_User():
    clear()

    print(f"""\n\n\n\n\n
O                                          O
:                                          :
:                  [{Palette_Warna("Green","•","Bold")}--]                   :
:__________________________________________:
|'            !Selamat Datang!            '|
|                                          |
|      Masuk ke dalam program sebagai:     |
|    [1] Pembeli            [2] Penjual    |
 \________________________________________/""")


    Respon_Menu_User = input("\n\t\t  >> ")
    if Respon_Menu_User == "1":
        #cls
        Login_Pembeli()
    elif Respon_Menu_User == "2":
        #cls
        Login_Penjual()
    else:
        printc ("LRed",f"\t  Menu < {Respon_Menu_User} > tidak tersedia","Bold")
        tclear(2)
        Menu_User()

def Menu_untuk_Pembeli(warning=""):
    clear()
    print(f""" 
    
    {warning}
    
    Berikut Opsi Interaktif Kami, {akun_now.nama}!!
    [1] Lihat daftar seluruh barang
    [2] Cari nama barang
    [3] Daftar pesanan
    [4] Keluar """)
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
        menu_searching()
    elif Respon_menu_user == "3":
        menu_pesanan_pembeli()
    elif Respon_menu_user == "4":
        # +Feedback
        Menu_User()
    else:
        Menu_untuk_Pembeli(warning="Opsi tidak tersedia!")

def Menu_untuk_Penjual(warning=""):
    clear()

    print(
        f""" 
    
        {warning}
        
        Berikut Opsi Interaktif Kami, {akun_now.nama}!!
        [1] Lihat daftar seluruh masker 
        [2] Cari masker
        [3] Daftar pesanan masuk
        [4] Keluar """
    )

    Respon_menu_user = input("\n\t\t>> ")

    if Respon_menu_user == "1":
        menu_sorting()
    elif Respon_menu_user == "2":
        menu_searching()
    elif Respon_menu_user == "3":
        menu_pesanan_penjual()
    elif Respon_menu_user == "4":
        # +Feedback
        Menu_User()
    else:
        Menu_untuk_Pembeli(
            warning="Opsi tidak tersedia!"
        )


# = = = = = = = = = = = = = = = = = MENU YANG SAMA = = = = = = = = = = = = = = = = = = 

# sorting masker + beli masker (pembeli) v edit masker (penjual)
def menu_sorting(warning=""):
    clear()

    print(f"""

    {warning}

    Pilih metode pengurutan barang:
    [1] Berdasarkan Nama
    [2] Berdasarkan Warna
    [3] Berdasarkan Ketersediaan / Stok
    [4] Berdasarkan Harga Terendah
    [5] Berdasarkan Harga Tertinggi
    [6] Kembali""")
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
        list_masker = sort_berdasarkan(indikator)
    elif kategori == "5":
        indikator = "harga (descending)"
        list_masker = sort_berdasarkan(indikator)
        list_masker = [list_masker[i] for i in range(len(list_masker)-1, -1, -1)]

    # kembali ke menu
    elif kategori == "6":
        if type(akun_now) == Pembeli:
            Menu_untuk_Pembeli()
        else:
            Menu_untuk_Penjual()
    # warning
    else:
        menu_sorting(warning="Opsi tidak tersedia!")

    tampilkan_daftar_masker(
        subjudul = f"Sort berdasarkan {indikator}.",
        list_masker = list_masker
    )

# search masker
def menu_searching(warning=""):
    clear()
    print(f"\t{warning}")
    Barang_dituju = input("\n Cari masker: ")
    print()

    # masker yg dicari ada
    if masker_tersedia(Barang_dituju):

        # tampilkan masker
        masker_ditemukan = masker_dipilih(Barang_dituju)
        tampilkan_daftar_masker(
            subjudul = f"Hasil pencarian '{Barang_dituju}.'",
            list_masker = masker_ditemukan
        )

    # masker yg dicari tidak ada
    else:

        #timed cls 1s
        for i in range(3,0,-1):
            print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")
        menu_searching()

# tampilan daftar masker
def tampilkan_daftar_masker(subjudul, list_masker, warning=""):
    clear()
    print("\tDaftar Masker")
    print("\t=============")
    print(f"\t{subjudul}")
    print(f"\t{warning}")

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
            list_masker
        )

    # di akun penjual --> tanyakan apakah ingin manipulasi masker
    else:
        pilih_masker(
            subjudul,
            list_masker
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
        print("\tAnda belum membeli barang.")
        
        input("\n\n\t\tKembali => ")
        Menu_untuk_Pembeli()
    # jika sudah pesan
    else:
        akun_now.tampilkan_pesanan()
        
        input("\n\n\t\tKembali =>")
        Menu_untuk_Pembeli()

# tanyakan apakah melakukan transaksi
def transaksi_pesanan(subjudul, list_masker):
    # pilihan setelah melihat daftar masker
    print(
        f"\n\t[1] Pesan masker\
        \n\t[2] Kembali"
    )
    respon = input("\n\t>> ")

    # jika pesan masker
    if respon == "1":
        kode_masker = input("\n\tKode masker\t: ")

        # cek kode ada atau tidak
        index_masker = fibonacci_search(
            list_data = [masker.kode for masker in daftar_masker],
            data = kode_masker
        )

        # jika masker ada
        if index_masker is not None:
            print() 

            masker = daftar_masker[index_masker]

            form = ["Jumlah barang", "Alamat Anda"]
            for i in range(len(form)):
                answer = input(f"\t{form[i].ljust(15)} : ")

                # jumlah yg dimasukkan
                if i == 0:
                    if jumlah_masuk_akal(answer) and answer <= masker.jumlah:
                        tampilkan_daftar_masker(
                            subjudul,
                            list_masker,
                            warning = "Stok tidak mencukupi!"
                        )
                    else:
                        tampilkan_daftar_masker(
                            subjudul,
                            list_masker,
                            warning = "Jumlah tidak valid"
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
                warning="Masker tidak ditemukan!"
            )

    # jika tidak pesan masker
    elif respon == "2":
        input("\n\t\tKembali => ")
        Menu_untuk_Pembeli()

    # jika opsi tidak tersedia
    else:
        tampilkan_daftar_masker(warning="Opsi tidak tersedia!")


# = = = = = = = = = = = = = = = = = = MENU.PENJUAL = = = = = = = = = = = = = = = = = = = 

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

            for pesanan in akun_now.list_pesanan:
                if no_pesanan == pesanan[1]:
                    akun_now.kirim_masker(
                        no_pesanan = no_pesanan,
                        jumlah = pesanan[4]
                    )

                    print(f"\nPesanan {no_pesanan} telah berhasil dikirim!")
            else:
                menu_pesanan_penjual(warning="Masker tidak ditemukan!")

        input("\n\n\t\tKembali =>")
        Menu_untuk_Penjual()

# masker yang mau diedit
def pilih_masker(subjudul, list_masker):
    # menu yang tersedia
    print(
        "\n\t[1] Ubah masker\
        \n\t[2] Kembali"
    )
    respon = input("\n\t>> ")
    
    # ubah masker
    if respon == "1":
        kode_masker = input("Kode masker : ")
        clear()

        # cek masker
        index_masker = fibonacci_search(
            list_data = [masker.kode for masker in daftar_masker],
            data = kode_masker
        )

        # edit masker yg dicari
        if index_masker is not None:
            edit_masker(daftar_masker[index_masker])

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
                warning = "Masker tidak ditemukan."
            )

    # kembali
    elif respon == "2":
        Menu_untuk_Penjual()

    # opsi tidak tersedia
    else:
        tampilkan_daftar_masker(
            subjudul, 
            list_masker,
            warning = "Opsi tidak tersedia!"
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
                masker.tambah_stok()

            else:
                edit_masker(
                    masker, 
                    warning="Jumlah tidak valid!"
                )

        except ValueError:
            edit_masker(
                masker, 
                warning="Jumlah tidak valid!"
            )
        
    # kurangi stok
    elif Respon_menu_user == "2":
        try:
            jumlah = int(input("Jumlah\t: "))

            if jumlah_masuk_akal(jumlah):
                masker.kurangi_stok()

            else:
                edit_masker(
                    masker, 
                    warning = "Jumlah tidak valid!"
                )
            
        except ValueError:
            edit_masker(
                masker, 
                warning = "Jumlah tidak valid!"
            )
    
    # hapus masker
    elif Respon_menu_user == "3":

        for mask in akun_now.list_masker:
            if mask == masker:
                print(f"{mask} telah berhasil dihapus.")
                akun_now.list_masker.remove(mask)

    # kembali ke menu            
    elif Respon_menu_user == "4":
        pass

    # opsi tidak tersedia
    else:
        edit_masker(
            masker, 
            warning="Opsi tidak tersedia!"
        )

# ==================================== START ====================================

if __name__ == "__main__":
    while True:
        Menu_User()