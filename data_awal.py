# RESET DATA =====================================

from sistem import *

akun_pembeli_baru(
    nama = "Aziizah",
    password = "004"
)
akun_pembeli_baru(
    nama = "Ibnu",
    password = "039"
)

# # masker = [nama, warna, harga, jumlah]
# masker = [
#     ["Masker KF94 10 Pcs", "Kuning", 10000, 300],
#     ["Masker KF94 10 Pcs", "Hitam", 10000, 300],
#     ["Masker KF94 10 Pcs", "Ayam Jago", 12000, 100],
#     ["Masker KF94 10 Pcs", "Navy", 12000, 100],
#     ["Masker KF94 10 Pcs", "Biru", 12000, 100],
#     ["Masker KF94 10 Pcs", "Hijau", 12000, 100],
#     ["Masker KF94 50 Pcs", "Kuning", 45000, 50],
#     ["Masker KF94 50 Pcs", "Hitam", 45000, 50],

#     ["Masker KN95 10 Pcs", "Kuning", 8000, 200],
#     ["Masker KN95 10 Pcs", "Hitam", 8000, 200],
#     ["Masker KN95 10 Pcs", "Ayam Jago", 10000, 100],
#     ["Masker KN95 10 Pcs", "Biru", 10000, 100],
#     ["Masker KN95 10 Pcs", "Kuning", 40000, 50],
#     ["Masker KN95 10 Pcs", "Hitam", 40000, 50],

#     ["Masker Duckbill 50 Pcs", "Kuning", 25000, 300],
#     ["Masker Duckbill 50 Pcs", "Hitam", 25000, 300],

#     ["Masker Bedah 50 Pcs", "Biru", 40000, 200],
#     ["Masker N95 50 Pcs", "Toska", 95000, 50],
#     ["Masker N98 2 Pcs", "Kuning", 20000, 50],
#     ["Masker N98 2 Pcs", "Hitam", 20000, 50],
#     ["Masker N98 2 Pcs", "Biru", 20000, 50],

#     ["Masker N100 1 Pcs", "Kuning", 300000, 20]
# ]

# for i in range(len(masker)):
#     akun_toko[0].tambah_masker_baru(
#         nama_masker = masker[i][0],
#         warna = masker[i][1],
#         harga = masker[i][2],
#         jumlah = masker[i][3],
#         kode = kode_masker(i+1, masker[i][1])
#     )

# =================== YG BISA DIPAKE YG BAWAH ====================

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
        jumlah = jumlah[i],
        kode = kode_masker(i+1, warna[i])
    )


