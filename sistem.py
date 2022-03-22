class Toko:
    def __init__(self, nama, lokasi):
        # identitas toko
        self.nama = nama
        self.lokasi = lokasi

        # persediaan toko
        self.barang = []
        self.pendapatan = 0
        self.pesanan = 0

    def tambah_barang_baru(self, barang, harga, jumlah):
        self.barang.append(Barang(barang, harga, jumlah))

    def kirim_barang(self, barang, jumlah):
        for x in self.barang:
            if x.nama == barang:
                x.jumlah -= jumlah
    
    def stok_barang(self, barang):
        objek = [x for x in self.barang if x.nama == barang]
        print(f"{objek[0].nama} --- stok saat ini : {objek[0].jumlah}")

class Barang:
    def __init__(self, nama, harga, jumlah):
        # identitas barang
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

        # rating pembelian barang
        self.nilai = 0
        self.terjual = 0
        self.rate = self.nilai/self.terjual if self.terjual != 0 else 0

    def tambah_jumlah(self, jumlah):
        self.jumlah += jumlah

    def kurangi_jumlah(self, jumlah):
        self.jumlah -= jumlah

class Pembeli:
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password
    
    def pesan_barang(self, toko, barang, jumlah):
        for x in toko.barang:
            if x.nama == barang:
                x.jumlah -= jumlah
                x.terjual += jumlah

    # 1 s/d 5
    def nilai_barang(self, toko, barang, nilai):
        for x in toko.barang:
            if x.nama == barang:
                x.nilai += nilai

        
toko1 = Toko("Ayam", "Samarinda")
toko1.tambah_barang_baru("Panci", 2000, 100)
toko1.stok_barang("Panci")
toko1.kirim_barang("Panci", 20)
toko1.stok_barang("Panci")

