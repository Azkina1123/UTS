# import sqlite3

# # connect database
# con = sqlite3.connect("database.db")
# cur = con.cursor()

# tabel_masker = '''CREATE TABLE tabel_masker (kode text, nama text, warna text, harga integer, jumlah integer)'''
# cur.execute(tabel_masker)

# tabel_pesanan_penjual = '''CREATE TABLE tabel_pesanan_penjual (tanggal text, nomor_pesanan text, masker text, jumlah integer, total integer, pembeli text, alamat text, status text)'''
# cur.execute(tabel_pesanan_penjual)

# tabel_akun_pembeli = '''CREATE TABLE tabel_akun_pembeli (nama text, password text)'''
# cur.execute(tabel_akun_pembeli)

# # simpan data
# con.commit()
# con.close()

# TAMBAH STOK =====================================

from sistem import *
nama = [
    "Masker KF94 10 Pcs", "Masker KF94 50 Pcs", 
    "Masker KN95 10 Pcs", "Masker KN95 50 Pcs"
]
warna = [
    "Putih", "Putih",
    "Putih", "Putih"
]
harga = [
    12000, 45000,
    10000, 40000
]
jumlah = [
    100, 500,
    150, 500
]

for i in range(len(nama)):
    akun_toko[0].tambah_masker_baru(
        nama_masker=nama[i],
        warna = warna[i],
        harga = harga[i],
        jumlah = jumlah[i]
    )
