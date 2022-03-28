import sqlite3

# connect database
con = sqlite3.connect("database.db")
cur = con.cursor()

tabel_masker = '''CREATE TABLE tabel_masker (kode text, nama text, warna text, harga integer, jumlah integer)'''
cur.execute(tabel_masker)

tabel_pesanan_penjual = '''CREATE TABLE tabel_pesanan_penjual (tanggal text, nomor_pesanan text, pembeli text, masker text, jumlah integer, alamat text, total integer)'''
cur.execute(tabel_pesanan_penjual)

tabel_akun_pembeli = '''CREATE TABLE tabel_akun_pembeli (nama text, warna text, harga integer, jumlah integer)'''
cur.execute(tabel_akun_pembeli)

tabel_pesanan_pembeli = '''CREATE TABLE tabel_pesanan_pembeli (tanggal text, nomor_pesanan text, masker text, jumlah integer, alamat text, total integer)'''
cur.execute(tabel_pesanan_pembeli)

# simpan data
con.commit()
con.close()