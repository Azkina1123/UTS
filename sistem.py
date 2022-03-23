class Toko:
    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, lokasi):
        # identitas toko
        self.nama = nama
        self.lokasi = lokasi

        # persediaan toko
        self.list_masker = [] # tempat objek masker yg dijual

        self.list_pesanan_masuk = []
        self.pesanan_masuk = len(self.list_pesanan_masuk)
        self.pendapatan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def tambah_masker_baru(self, nama_masker, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, harga, jumlah))

    def tambah_pesanan_masuk(self, nama_masker, jumlah, alamat):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                # persediaan masker dikurangi
                masker.kurangi_stok(jumlah)

                pesanan = [nama_masker, jumlah, alamat]
                self.list_pesanan_masuk.append(pesanan)

                self.pendapatan += jumlah * masker.harga

    def kirim_masker(self):
        pass
    
    def restock_masker(self, nama_masker, jumlah):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                masker.tambah_stok(jumlah)
    
    def stok_masker(self, nama_masker):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                return masker.jumlah

    def stok_toko(self):
        if len(self.list_masker) != 0:
            for masker in self.list_masker:
                print(f"{masker.nama} saat ini = {masker.jumlah} buah")
        else:
            print("Toko belum memiliki barang yang dijual.")


class Masker:
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_stok(self, jumlah):
        self.jumlah += jumlah

    def kurangi_stok(self, jumlah):
        self.jumlah -= jumlah


class Pembeli:
    # default attribute/properties tiap2 akun pembeli ------------------------
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, nama_masker, jumlah, alamat):
        for masker in toko.list_masker:
            if masker.nama == nama_masker:
                toko.tambah_pesanan_masuk(nama_masker, jumlah, alamat)


def search():
    pass

def sort():
    pass

# contoh -----------------------------------------------------------------------------

# buat toko .........................................
toko_ayam = Toko("Ayam", "Samarinda") # nama toko = Ayam, lokasi = Samarinda

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


# buat akun pembeli ...............................
yapi = Pembeli("Yapi", 123)
# nama pembeli = Yapi, password = 123

print("\nYapi pesan masker...")
# yapi beli Masker Biru dari Toko Ayam 50 buah ke alamat Samarinda
yapi.pesan_masker(toko_ayam, "Masker Biru", 50, "Samarinda")
# yapi beli Masker Hijau dari Toko Ayam 30 buah ke alamat Samarinda
yapi.pesan_masker(toko_ayam, "Masker Hijau", 30, "Samarinda")

# cek persediaan toko lagi
print("\nCek persediaan...")
print("Stok Toko Ayam : ")
toko_ayam.stok_toko()




