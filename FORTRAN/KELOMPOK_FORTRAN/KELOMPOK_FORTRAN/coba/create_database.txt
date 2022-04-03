import sqlite3

# connect database
con = sqlite3.connect("database.db")
cur = con.cursor()

tabel_masker = '''CREATE TABLE tabel_masker (kode text, nama_masker text, warna text, harga integer, jumlah integer)'''
cur.execute(tabel_masker)

tabel_pesanan_penjual = '''CREATE TABLE tabel_pesanan_penjual (tanggal text, nomor_pesanan text, nama_masker text, warna_masker text, jumlah integer, total integer, pembeli text, alamat text, status text)'''
cur.execute(tabel_pesanan_penjual)

tabel_akun_pembeli = '''CREATE TABLE tabel_akun_pembeli (nama text, password text)'''
cur.execute(tabel_akun_pembeli)

# simpan data
con.commit()
con.close()