from sistem import *

# Menu?
def Menu_User():
    clear()

    print("""\n\n\n\n\n
            !Selamat Datang!

      Masuk ke dalam program sebagai:
    [1] Pembeli            [2] Penjual""")

    Respon_Menu_User = input("\n\t\t >> ")
    if Respon_Menu_User == "1":
        #cls
        Login_Pembeli()
    elif Respon_Menu_User == "2":
        #cls
        Login_Penjual()
    else:
        print (f"Menu < {Respon_Menu_User} > tidak tersedia")
        #timed_cls
        Menu_User()

akun_pembeli_now = None
def Login_Pembeli(warning=""):
    global akun_pembeli_now
    clear()

    print("\n\n\n\n\n")
    print(warning.center(30))
    print("""
    Pilih metode masuk:
    [1] Login   [3] Kembali
    [2] Sign-up
    """)

    # masukkan opsi
    Respon_menu_user = input("\n    >> ")

    # opsi tidak tersedia
    if Respon_menu_user not in ("1", "2", "3"):
        Login_Pembeli("Opsi tidak tersedia!")
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
                Login_Pembeli("Aktivitas dibatalkan.")
            else:
                form[i] = answer

        nama, password = tuple(form)

        # kalau mau login
        if Respon_menu_user == "1":
            #Verifikasi nama+pass / pembatalan pilihan --> 
            if nama_sudah_ada(akun_pembeli, nama) and password_benar(akun_pembeli, nama, password):
                # berhasil masuk, sekarang di akun si yg namanya diinput tadi
                akun_pembeli_now = [pembeli for pembeli in akun_pembeli if pembeli.nama == nama]

                Menu_untuk_Pembeli()

            else:
                Login_Pembeli("Gagal log in!")
        
        # kalau mau sign up
        elif Respon_menu_user == "2":

            #Verifikasi apakah nama sudah tersedia atau belum
            if nama_sudah_ada(akun_pembeli, nama):
                Login_Pembeli("Gagal sign up!")
            else:
                # buat akun. masukkan ke list akun_pembeli di sistem
                akun_baru = Pembeli(nama, password)
                akun_pembeli.append(akun_baru)
                Login_Pembeli("Sign up berhasil!")
            

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
            Login_Penjual("Aktivitas dibatalkan.")
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



#------------------------- Menu Sebenarnya -------------------------#

# = = = = = = = = = = = = = = = = = = MENU PEMBELI = = = = = = = = = = = = = = = = = = 


def Menu_untuk_Pembeli(Notes="Selamat datang ((Pembeli))!!"):
    clear()

    print(f""" {Notes}
    [1] Pilih kategori barang
    [2] Cari barang berdasarkan nama
    [3] Cek daftar barang secara keseluruhan
    [4] Menuju struk belanja
    [5] Keluar """)
    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    Respon_menu_user = input("\n\t\t>> ")
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

    if Respon_menu_user == "1":
        Menu_pembeli_1()
    elif Respon_menu_user == "2":
        Menu_pembeli_2()
    elif Respon_menu_user == "3":
        Menu_pembeli_3()
    elif Respon_menu_user == "4":
        Menu_pembeli_4()
    elif Respon_menu_user == "5":
        Menu_User()
    else:
        Menu_untuk_Pembeli()

# pilih kategori barang
def Menu_pembeli_1(warning=""):
    clear()
    #pilih kategori(Nama, Warna)
    print("\n\n\n")
    print(warning.center(30))
    print("\n\
            Pilih kategori : \n\
            [1] Nama\t[2] Warna]")
    kategori = input("\n\t>> ")

    if kategori == "1":
        pass
    elif kategori == "2":
        pass
    

def Menu_pembeli_2():
    clear()
    Barang_dituju = input("\n Cari barang: ")
    #cls

    #if Barang_dituju in ListBarang --> "\n\n\t\tbarang ditemukan!: ", tampilkan barang dan stok
    if masker_tersedia(Barang_dituju):

    # tampilkan masker-masker yang namanya berkaitan dgn yg dicari
        masker_ditemukan = masker_dipilih(Barang_dituju)
        i = 1
        for masker in masker_ditemukan:
            print(f"---- {i} ----".center(30))
            masker.tampilkan_data() # di class Pembeli
            print()
            i += 1

        # user pilih masker mana yg mau dibeli
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
                        answer = int(answer)
                        form[i] = answer
                
                """ PROSES PEMBELIAN
                akun_pembeli_now[0] = akun yg login
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
                    akun_pembeli_now[0].pesan_masker(akun_toko[0], kode_masker, form[0], form[1])

                    Menu_pembeli_1()
                    
                else:
                    # pesanan batal
                    Menu_pembeli_2()

            # barang yg dibeli gak ada
        else:
            # barang g ada
            Menu_pembeli_2()

    # #if Barang_dituju not in ListBarang -->
    else:
        for i in range(3,0,-1):
            print(f"\n\n \t\tBarang tidak ditemukan atau sedang tidak tersedia ({i}s)")

    #timed cls 1s

    
def Menu_pembeli_3():
    print( """Pilih metode pengurutan barang:
    [1] Berdasarkan Nama
    [2] Berdasarkan Warna
    [3] Berdasarkan Ketersediaan / Stok
    [4] Berdasarkan Harga Terendah
    [5] Berdasarkan Harga Tertinggi""")
    #Sort barang berdasarkan? (Nama, Warna, Stok, Best seller(?), harga)
    #if-if-if-if
    pass

def Menu_pembeli_4():
    #strukbelanja(For i in struk belanja, terurut berdasarkan waktu pemesanan)
    pass


# = = = = = = = = = = = = = = = = = = MENU PENJUAL = = = = = = = = = = = = = = = = = = 

def Menu_untuk_Penjual(Notes="Selamat datang kembali ((Penjual))!!"):
    clear()

    print(f""" {Notes}
    [1] Tambahkan masker baru
    [2] Hapus masker yang sudah ada""")
    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    Respon_menu_user = int(input("\n\t\t>>"))
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

Login_Pembeli()