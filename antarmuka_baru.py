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

# pilih sorting berdasarkan apa
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
        if type(akun_now) == Pembeli:
            Menu_untuk_Pembeli()
        else:
            Menu_untuk_Penjual()
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
        konfirmasi_pesanan(menu_sorting, Menu_untuk_Pembeli)
    else:
        input("\n\t\tKembali =>")
        Menu_untuk_Penjual()
    
# search masker
def menu_searching(warning=""):
    clear()
    print(f"\t{warning}")
    Barang_dituju = input("\n Cari masker: ")
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
        if type(akun_now) == Pembeli:
            konfirmasi_pesanan(menu_searching, Menu_untuk_Pembeli)
        else:
            input("\n\t\tKembali => ")
            Menu_untuk_Penjual()

    # #if Barang_dituju not in ListBarang -->
    else:

        #timed cls 1s
        for i in range(3,0,-1):
            print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")
        menu_searching()

# daftar pesanan pembeli
def menu_pesanan_pembeli():
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
        Menu_untuk_Pembeli()

def konfirmasi_pesanan(menu_refresh, menu_back):
    print(
        "\n\t[1] Pesan masker\
        \n\t[2] Kembali"
    )
    respon = input("\n\t>> ")

    if respon == "1":
        kode_masker = input("\n\tKode masker\t: ")

        for masker in daftar_masker:
            if masker.kode == kode_masker:
                print()

                # lanjutkan pembelian
                form = ["Jumlah barang", "Alamat Anda"]
                for i in range(len(form)):
                    answer = input(f"\t{form[i].ljust(15)} : ")

                    if i == 0:
                        try:
                            answer = int(answer)
                        except ValueError:
                            menu_refresh(warning="Jumlah barang salah!")

                        if answer >= masker.jumlah:
                            menu_refresh("Stok tidak mencukupi!")
                        elif jumlah_masuk_akal(answer) or answer <= masker.jumlah:
                            pass
                        else:
                            menu_refresh("Jumlah barang salah!")
                        
                    form[i] = answer
                    
                """ PROSES PEMBELIAN
                akun_now = akun yg login
                akun_toko[0]        = akun toko ini
                form[0]             = jumlah barang
                form[1]             = alamat barang
                """

                print(f"Total yang harus dibayar adalah Rp{form[0]*masker.harga}")
                respon = input("\nKetik '1' untuk melanjutkan pembelian\n>> ")
        
                if respon == "1":
                    # pesanan diproses
                    akun_now.pesan_masker(akun_toko[0], kode_masker, form[0], form[1])
                    Menu_untuk_Pembeli(warning="Pembelian berhasil!")

                else:
                    # pesanan batal
                    menu_refresh(warning="Pembelian dibatalkan.")
        else:
            # barang g ada
            menu_refresh(warning="Masker tidak ditemukan!")
    else:
        input("\n\t\tKembali => ")
        menu_back()
        
# = = = = = = = = = = = = = = = = = = MENU PENJUAL = = = = = = = = = = = = = = = = = = 

def Menu_untuk_Penjual(warning=""):
    clear()

    print(f""" 
    
    {warning}
    
    Berikut Opsi Interaktif Kami, {akun_now.nama}!!
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
        Menu_untuk_Pembeli(warning="Opsi tidak tersedia!")

    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

def pilih_masker(menu):
    kode_masker = input("Pilih kode masker : ")
    clear()

    # tampilkan spek masker
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
    [4] Kembali """)

    Respon_menu_user = input("\n\t\t>> ")
    print()
    if Respon_menu_user == "1":
        try:
            jumlah = int(input("Jumlah\t: "))
        except ValueError:
            edit_masker(masker, warning="Jumlah tidak valid!")
        
        if jumlah_masuk_akal(jumlah):
            masker.tambah_stok()
        else:
            edit_masker(masker, warning="Jumlah tidak valid!")

    elif Respon_menu_user == "2":
        try:
            jumlah = int(input("Jumlah\t: "))
        except ValueError:
            edit_masker(masker, warning="Jumlah tidak valid!")
        
        if jumlah_masuk_akal(jumlah):
            masker.kurangi_stok()
        else:
            edit_masker(masker, warning="Jumlah tidak valid!")
    elif Respon_menu_user == "3":
        for mask in akun_now.list_masker:
            if mask == masker:
                print(f"{mask} telah berhasil dihapus.")
                akun_now.list_masker.remove(mask)
    elif Respon_menu_user == "4":
        pass
    else:
        edit_masker(masker, warning="Opsi tidak tersedia!")

def menu_pesanan_penjual(warning=""):
    clear()
    print("\n\n\tDaftar Pesanan Masuk")
    print("\t===================\n")
    print(f"{warning}")

    if len(akun_now.list_pesanan) == 0:
        print("\tBelum ada pesanan masuk.")
        input("\n\n\t\tKembali => ")
        Menu_untuk_Penjual()
    else:
        akun_now.tampilkan_pesanan()

        respon = input("\n\nKetik '1' untuk mengirim masker\n\t>> ")
        if respon == "1":
            no_pesanan = input("Nomor pesanan\t:")
            list_no_pesanan = [isi[1] for isi in akun_now.list_pesanan]
            list_jumlah = [isi[4] for isi in akun_now.list_pesanan]

            index = list_no_pesanan.index(no_pesanan)
            
            if no_pesanan in list_no_pesanan:
                akun_now.kirim_masker(no_pesanan, list_jumlah[index])

                print(f"\nPesanan {no_pesanan} telah berhasil dikirim!")
            else:
                menu_pesanan_penjual("Masker tidak ditemukan!")
        
        else:
            pass

        input("\n\n\t\tKembali =>")
        Menu_untuk_Penjual(akun_now)


Menu_User()