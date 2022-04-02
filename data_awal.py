from sistem import kode_masker
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
        nama_masker=masker[i][0],
        warna = masker[i][1],
        harga = masker[i][2],
        jumlah = masker[i][3],
        kode = kode_masker(i+1, masker[i][1])
    )


