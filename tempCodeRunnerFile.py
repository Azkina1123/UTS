
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


