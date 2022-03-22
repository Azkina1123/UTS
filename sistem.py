class Toko:

    # default attribute/properties toko -----------------------------------
    def __init__(self, nama, lokasi):
        # identitas toko
        self.nama = nama
        self.lokasi = lokasi

        # persediaan toko
        self.list_masker = [] # tempat objek masker yg dijual
        self.pendapatan = 0
        self.pesanan = 0

    # method = fungsi yg cuma bisa dipake objek Toko ----------------------
    def tambah_masker_baru(self, nama_masker, harga, jumlah):
        self.list_masker.append(Masker(nama_masker, harga, jumlah))

    def kirim_masker(self, nama_masker, jumlah):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                masker.jumlah -= jumlah
    
    def stok_tersedia(self, nama_masker):
        for masker in self.list_masker:
            if masker.nama == nama_masker:
                print(f"{masker.nama} --- stok saat ini : {masker.jumlah}")


class Masker:
    # default attribute/properties tiap2 masker -----------------------------
    def __init__(self, nama, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

        # rating pembelian barang
        self.nilai = 0
        self.terjual = 0
        self.rate = self.nilai/self.terjual if self.terjual != 0 else 0

    # method = fungsi yg cuma bisa dipake objek Masker -----------------------
    def tambah_persediaan(self, jumlah):
        self.jumlah += jumlah

    def kurangi_persediaan(self, jumlah):
        self.jumlah -= jumlah


class Pembeli:
    # default attribute/properties tiap2 akun pembeli ------------------------
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
    
    # method = semua yg bisa dilakukan oleh si pembeli -----------------------
    def pesan_masker(self, toko, nama_masker, jumlah):
        for masker in toko.list_masker:
            if masker.nama == nama_masker:
                masker.jumlah -= jumlah
                masker.terjual += jumlah

    # 1 s/d 5
    def nilai_masker(self, toko, nama_masker, nilai):
        for masker in toko.lis_masker:
            if masker.nama == nama_masker:
                masker.nilai += nilai

# contoh ----------------------------------------------------

# buat toko
toko1 = Toko("Ayam", "Samarinda")
toko1.tambah_barang_baru("Panci", 2000, 100)
toko1.stok_barang("Panci")
toko1.kirim_barang("Panci", 20)
toko1.stok_barang("Panci")

yapi = Pembeli("Yapi", 123)


