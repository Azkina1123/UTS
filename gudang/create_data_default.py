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

# masker = [nama, warna, harga, jumlah]
masker = [
    ["Masker KF94 10 Pcs", "Putih", 10000, 300],
    ["Masker KF94 10 Pcs", "Hitam", 10000, 300],
    ["Masker KF94 10 Pcs", "Abu-abu", 12000, 100],
    ["Masker KF94 10 Pcs", "Navy", 12000, 100],
    ["Masker KF94 10 Pcs", "Biru", 12000, 100],
    ["Masker KF94 10 Pcs", "Hijau", 12000, 100],
    ["Masker KF94 50 Pcs", "Putih", 45000, 50],
    ["Masker KF94 50 Pcs", "Hitam", 45000, 50],

    ["Masker KN95 10 Pcs", "Putih", 8000, 200],
    ["Masker KN95 10 Pcs", "Hitam", 8000, 200],
    ["Masker KN95 10 Pcs", "Abu-abu", 10000, 100],
    ["Masker KN95 10 Pcs", "Biru", 10000, 100],
    ["Masker KN95 10 Pcs", "Putih", 40000, 50],
    ["Masker KN95 10 Pcs", "Hitam", 40000, 50],

    ["Masker Duckbill 50 Pcs", "Putih", 25000, 300],
    ["Masker Duckbill 50 Pcs", "Hitam", 25000, 300],

    ["Masker Bedah 50 Pcs", "Biru", 40000, 200],
    ["Masker N95 50 Pcs", "Toska", 95000, 50],
    ["Masker N98 2 Pcs", "Putih", 20000, 50],
    ["Masker N98 2 Pcs", "Hitam", 20000, 50],
    ["Masker N98 2 Pcs", "Biru", 20000, 50],

    ["Masker N100 1 Pcs", "Putih", 300000, 20]
]

for i in range(len(masker)):
    akun_toko[0].tambah_masker_baru(
        nama_masker = masker[i][0],
        warna = masker[i][1],
        harga = masker[i][2],
        jumlah = masker[i][3],
        kode = kode_masker(i+1, masker[i][1])
    )

# =================== YG BISA DIPAKE YG BAWAH ====================

# nama = [
#     "Masker KF94 10 Pcs", "Masker KF94 50 Pcs", 
#     "Masker KN95 10 Pcs", "Masker KN95 50 Pcs"
# ]
# warna = [
#     "Putih", "Putih",
#     "Putih", "Putih"
# ]
# harga = [
#     12000, 45000,
#     10000, 40000
# ]
# jumlah = [
#     100, 500,
#     150, 500
# ]

# ======================== BY YAPI ============================

# nama = [
#     "Masker KF94 10 Pcs", "Masker KF94 10 Pcs", "Masker KF94 10 Pcs", 
#     "Masker KF94 10 Pcs", "Masker KF94 10 Pcs", "Masker KF94 10 Pcs", 
#     "Masker KF94 50 Pcs", "Masker KF94 50 Pcs",

#     "Masker KN95 10 Pcs", "Masker KN95 10 Pcs", "Masker KN95 10 Pcs",
#     "Masker KN95 10 Pcs", "Masker KN95 10 Pcs", "Masker KN95 10 Pcs",

#     "Masker Duckbill 50 Pcs", "Masker Duckbill 50 Pcs",

#     "Masker Bedah 50 Pcs",

#     "Masker N95 50 Pcs",

#     "Masker N98 2 Pcs", "Masker N98 2 Pcs", "Masker N98 2 Pcs",

#     "Masker N100 1 Pcs"
# ]
# warna = [
#     "Putih", "Hitam", "Abu-abu",
#     "Navy", "Biru", "Hijau",
#     "Putih", "Hitam",

#     "Putih", "Hitam", "Abu-abu",
#     "Biru", "Putih", "Hitam",

#     "Putih", "Hitam",

#     "Biru",
    
#     "Toska",
    
#     "Putih", "Hitam", "Biru",

#     "Putih"
# ]
# harga = [
#     10, 10, 12,
#     12, 12, 12,
#     45, 45,

#     8, 8, 10,
#     10, 40, 40,

#     25, 25,

#     40,

#     95,

#     20, 20, 20,
    
#     300

# ]
# jumlah = [
#     300, 300, 100,
#     100, 100, 100,
#     50, 50,

#     200, 200, 100,
#     100, 50, 50,

#     25, 25,

#     300,

#     200,

#     50, 50, 50,
    
#     20
# ]

# for i in range(len(nama)):
#     akun_toko[0].tambah_masker_baru(        
#         nama_masker=nama[i],
#         warna = warna[i],
#         harga = harga[i],
#         jumlah = jumlah[i],
#         kode = kode_masker(i+1, warna[i])
#     )


