from sistem import *

# Menu?
def Menu_User():
    clear()

    print("""\n\n\n\n\n
            !Selamat Datang!

      Masuk ke dalam program sebagai:
    [1] Pembeli            [2] Penjual""")

    Respon_Menu_User = int(input("\n\t\t >> "))
    if Respon_Menu_User == 1:
        #cls
        Login_Pembeli()
    elif Respon_Menu_User == 2:
        #cls
        Login_Penjual()
    else:
        print (f"Menu < {Respon_Menu_User} > tidak tersedia")
        #timed_cls
        Menu_User()

def Login_Pembeli():
    clear()
    
    print("""\n\n\n\n\n


    Pilih metode masuk:
    [1] Login   [2] Sign-up
    """)
    Respon_menu_user = int(input("\n\t\t >> "))
    if Respon_menu_user == 1:
        print()
        #input(Nama)
        #input(Password)
        nama = input("Nama : ")
        password = input("Password : ")

        #Verifikasi nama+pass / pembatalan pilihan --> Login_Pembeli()
        if nama_sudah_ada(akun_pembeli, nama) and password_benar(akun_pembeli, nama, password):
            print("Berhasil masuk")
        
        else:
            print("Gagal login")
            #cls, Menu_untuk_pembeli()
            
    
    elif Respon_menu_user == 2:
        print()

        #input(Nama)
        #input(Password)
        nama = input("Nama : ")
        password = input("Password : ")

        #Verifikasi apakah nama sudah tersedia atau belum
        if nama_sudah_ada(akun_pembeli, nama):
            print("Gagal sign up")
            #cls, Login_Pembeli()
            pass
        else:
            print("Berhasil sign up")
            # buat akun. masukkan ke list akun_pembeli di sistem
            akun_baru = Pembeli(nama, password)
            akun_pembeli.append(akun_baru)


def Login_Penjual():
    print("""\n\n\n\n\n


    <Konfirmasi Identitas> """)
   #input(Nama)
   #input(Password)

    nama = input("Nama : ")
    password = input("Password : ")

   #Verifikasi nama+pass / pengusiran paksa
    if nama_sudah_ada(akun_toko, nama) and password_benar(akun_toko, nama, password):
        # berhasil masuk
        pass
    else:
        # gagal masuk
        pass



#------------------------- Menu Sebenarnya -------------------------#


def Menu_untuk_Pembeli(Notes="Selamat datang ((Pembeli))!!"):
    clear()

    print(f""" {Notes}
    [1] Pilih kategori barang
    [2] Cari barang berdasarkan nama
    [3] Cek daftar barang secara keseluruhan
    [4] Menuju struk belanja
    [5] Ubah profil
    [6] Keluar """)
    #note: 1 --> barang dipisah berdasarkan nama masker
    #      2 --> search nama barang
    #      3 --> tanya di-sort berdasarkan apa --> 
    #      4 --> tertera
    #      5 --> tertera
    Respon_menu_user = int(input("\n\t\t>>"))
    # Conditions Respon_menu_user
    # invalid_input --> Menu_untuk_pembeli("Silahkan pilih menu yang tersedia, ((Pembeli))")

def Menu_pembeli_1():
    #cls
    #pilih kategori(Nama, Warna)
    pass

def Menu_pembeli_2():
    Barang_dituju = input("\n Masukkan nama barang: ")
    #cls
    
    #if Barang_dituju in ListBarang --> "\n\n\t\tbarang ditemukan!: ", tampilkan barang dan stok
    if masker_tersedia(Barang_dituju):

        # tampilkan masker-masker yang namanya berkaitan dgn yg dicari
        masker_ditemukan = masker_dipilih(Barang_dituju)
        for masker in masker_ditemukan:
            masker.tampilkan_data() # di class Pembeli
            print()
            
        # user pilih masker mana yg mau dibeli
        #Apakah ingin menambahkan ke kereta belanja?
    
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

# Menu_User()

Menu_User()