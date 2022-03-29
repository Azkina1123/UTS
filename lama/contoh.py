from sistem import *

# contoh -----------------------------------------------------------------------------

# buat toko .........................................
toko_ayam = Toko("Ayam", "Samarinda") # nama toko = Ayam, lokasi = Samarinda
#????????????????????????????????????????????????????????????#

# cek persediaan awal toko
print("Cek persediaan...")
toko_ayam.stok_toko()

print("\nTambah masker yang akan dijual...")
toko_ayam.tambah_masker_baru("Masker Biru", 1000, 100)
# nama masker = Masker Biru, harga = 1000, persediaan = 100

toko_ayam.tambah_masker_baru("Masker Hijau", 2000, 50)
# nama masker = Masker Hijau, harga = 2000, persediaan = 50

# cek persediaan toko
print("\nCek persediaan...")
print("Stok Toko Ayam : ")
toko_ayam.stok_toko()


# buat akun pembeli ...................
yafi = Pembeli("Yafi", 123)
# nama pembeli = Yafi, password = 123

print("\nYapi pesan masker...")
# yapi beli Masker Biru 50 buah
yafi.pesan_masker(toko_ayam, "Masker Biru", 50)
# yapi beli Masker Biru dari Toko Ayam 30 buah
yafi.pesan_masker(toko_ayam, "Masker Hijau", 30)

# cek persediaan toko lagi
print("\nCek persediaan...")
print("Stok Toko Ayam : ")
toko_ayam.stok_toko()