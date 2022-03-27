from errno import EMEDIUMTYPE
from sistem import *

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
                Menu_untuk_Pembeli(akun_now.nama)

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
    global gagal_masuk_toko

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
        Menu_untuk_Penjual()

    else:
        # gagal masuk
        gagal_masuk_toko += 1

        # pengusiran paksa
        if gagal_masuk_toko == 3:
            exit()

        Login_Penjual(f"Gagal login ({gagal_masuk_toko})")


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



#------------------------- Menu Sebenarnya -------------------------#

# = = = = = = = = = = = = = = = = = = MENU PEMBELI = = = = = = = = = = = = = = = = = = 


def Menu_untuk_Pembeli(pembeli="Pembeli", warning=""):
    clear()

    print(f""" 
    
    {warning}
    
    Berikut Opsi Interaktif Kami, {pembeli}!!
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
        Menu_untuk_Pembeli(akun_now.nama, "Opsi tidak tersedia!")

# pilih kategori barang
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
    #if-if-if-if)

    list_masker = None
    if kategori == "1":
        list_masker = sort_berdasarkan("nama")
    elif kategori == "2":
        list_masker = sort_berdasarkan("warna")
    elif kategori == "3":
        list_masker = sort_berdasarkan("stok")
    elif kategori == "4":
        list_masker = sort_berdasarkan("harga")
    elif kategori == "5":
        list_masker = sort_berdasarkan("harga")
        list_masker = [list_masker[i] for i in range(len(list_masker)-1, -1, -1)]
    elif kategori == "6":
        Menu_untuk_Pembeli(akun_now.nama)
    else:
        menu_sorting("Opsi tidak tersedia!")

    # tampilkan daftar masker
    clear()
    print("\tDaftar Masker")
    print("\t=============")
    i = 1
    for masker in list_masker:
        print(f"\t---- {i} -----")
        masker.tampilkan_data()
        print()
        i += 1

    if type(akun_now) == Pembeli:
        # tanyakan apakah mau beli
        konfirmasi_pesanan(menu_sorting)
    else:
        pilih_masker = input("Pilih kode masker : ")
    
def menu_searching(warning=""):
    clear()
    print(f"\t{warning}")
    Barang_dituju = input("\n Cari barang: ")
    print()
    #cls

    #if Barang_dituju in ListBarang --> "\n\n\t\tbarang ditemukan!: ", tampilkan barang dan stok
    if masker_tersedia(Barang_dituju):

    # tampilkan masker-masker yang namanya berkaitan dgn yg dicari
        masker_ditemukan = masker_dipilih(Barang_dituju)
        print(("█"*50).center(30))
        i = 1
        for masker in masker_ditemukan:
            print(f"---- {i} ----".center(30))
            masker.tampilkan_data() # di class Pembeli
            print()
            print(("█"*50).center(30))
            i += 1

        # user pilih masker mana yg mau dibeli
        konfirmasi_pesanan(menu_searching)

    # #if Barang_dituju not in ListBarang -->
    else:
        for i in range(3,0,-1):
            print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")

    #timed cls 1s

# daftar pesanan pembeli
def menu_pesanan_pembeli(warning=""):
    clear()
    print("\n\n\tDaftar Pesanan Anda")
    print("\t===================\n")
    if len(akun_now.list_pesanan) == 0:
        print("\tAnda belum membeli barang.")
        input("\n\n\t\tKembali => ")
        Menu_untuk_Pembeli()
    else:
        akun_now.tampilkan_pesanan()
        input("\n\n\t\tKembali =>")
        Menu_untuk_Pembeli(akun_now)


def konfirmasi_pesanan(menu):
    respon = input("\tKetik '1' jika ingin membeli\n\t>> ")
    if respon == "1":
        print("\n(Masukkan kode masker)")
        kode_masker = input("Barang yang ingin dibeli : ")

        for masker in daftar_masker:
            if masker.kode == kode_masker:
                print()

                # lanjutkan pembelian
                form = ["Jumlah barang", "Alamat Anda"]
                for i in range(len(form)):
                    answer = input(f"{form[i].ljust(10)} : ")

                    if i == 0:
                        try:
                            answer = int(answer)
                        except ValueError:
                            menu(warning="Jumlah barang salah!")

                        if jumlah_masuk_akal(answer):
                            pass
                        else:
                            menu_searching()
                        
                    form[i] = answer
                    
                """ PROSES PEMBELIAN
                akun_now = akun yg login
                akun_toko[0]        = akun toko ini
                form[0]             = jumlah barang
                form[1]             = alamat barang
                """

                print(f"\nAnda memesan {masker.nama} warna {masker.warna}\
                    \nseharga Rp{masker.harga} sebanyak {form[0]} buah ke alamat {form[1]}.\
                    \nTotal yang harus dibayar adalah Rp{form[0]*masker.harga}")
                respon = input("\nKetik '1' untuk melanjutkan pembelian\n>> ")
        
                if respon == "1":
                    # pesanan diproses
                    akun_now.pesan_masker(akun_toko[0], kode_masker, form[0], form[1])
                    Menu_untuk_Pembeli(akun_now.nama, "Pembelian berhasil!")

                else:
                    # pesanan batal
                    menu(warning="Pembelian dibatalkan.")
        else:
            # barang g ada
            menu(warning="Masker tidak ditemukan!")
    else:
        menu()


        
# = = = = = = = = = = = = = = = = = = MENU PENJUAL = = = = = = = = = = = = = = = = = = 

def Menu_untuk_Penjual(penjual="Penjual", warning=""):
    clear()

    print(f""" 
    
    {warning}
    
    Berikut Opsi Interaktif Kami, {penjual}!!
    [1] Lihat daftar seluruh masker
    [2] Cari masker
    [3] Daftar pesanan masuk
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
        menu_pesanan_penjual()
    elif Respon_menu_user == "4":
        # +Feedback
        Menu_User()
    else:
        Menu_untuk_Pembeli(akun_now.nama, "Opsi tidak tersedia!")

    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    Respon_menu_user = int(input("\n\t\t>>"))
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

def pilih_masker(menu):
    kode_masker = input("Pilih kode masker : ")
    clear()

    for masker in daftar_masker:
        if masker.kode == kode_masker:
            edit_masker(masker)
    else:
        menu(warning="Masker tidak ditemukan.")

def edit_masker(masker, warning=""):
    clear()

    print("\n\n")
    masker.tampilkan_data()

    print(f""" 

    {warning}
    
    [1] Tambah stok masker
    [2] Kurangi stok masker
    [3] Hapus masker
    [4] Keluar """)

    Respon_menu_user = input("\n\t\t>> ")
    if Respon_menu_user == "1":
        pass
    elif Respon_menu_user == "2":
        pass
    elif Respon_menu_user == "3":
        pass
    elif Respon_menu_user == "4":
        pass
    else:
        edit_masker(masker, warning="Opsi tidak tersedia!")

def menu_pesanan_penjual(warning=""):
    clear()
    print("\n\n\tDaftar Pesanan Masuk")
    print("\t===================\n")
    if len(akun_now.list_pesanan) == 0:
        print("\tBelum ada pesanan masuk.")
        input("\n\n\t\tKembali => ")
        Menu_untuk_Penjual()
    else:
        akun_now.tampilkan_pesanan()

        respon = input("Ketik '1' untuk mengirim masker\n\t>> ")
        if respon == "1":
            kode_masker = input("Pilih nomor pesanan\t:")
            list_kode_masker = [masker.kode for masker in daftar_masker]
            if kode_masker in list_kode_masker:
                akun_now.kirim_masker()
            else:
                menu_pesanan_penjual("Masker tidak ditemukan!")
        else:
            pass
        input("\n\n\t\tKembali =>")
        Menu_untuk_Penjual(akun_now)


Menu_untuk_Pembeli()