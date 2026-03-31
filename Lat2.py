class RakGudang:
    def __init__(self):
        self.rak = [None] * 5

    def __setitem__(self, index, barang):
        if 0 <= index <= 4:
            self.rak[index] = barang
            print(f"'{barang}' berhasil disimpan di rak nomor {index}.")
        else:
            print(f"Gagal: Nomor rak {index} tidak tersedia. Pilih rak 0 - 4.")

    def __getitem__(self, index):
        if 0 <= index <= 4:
            barang = self.rak[index]
            return barang if barang is not None else "Kosong"
        else:
            return "Indeks rak tidak valid"

    def tampilkan_isi_rak(self):
        print("\n=== Daftar Isi Rak Gudang ===")
        for i in range(5):
            status = self.rak[i] if self.rak[i] is not None else "Kosong"
            print(f"Rak {i}: {status}")


gudang_dinda = RakGudang()

print("--- Proses Penyimpanan Barang ---")
gudang_dinda[0] = "Kardus Sepatu"
gudang_dinda[2] = "Alat Tulis"
gudang_dinda[4] = "Buku Cetak"
gudang_dinda[5] = "Barang Ilegal" 

print("\n--- Proses Mengambil/Mengecek Barang ---")
print(f"Cek rak nomor 2: {gudang_dinda[2]}")
print(f"Cek rak nomor 1: {gudang_dinda[1]}")

gudang_dinda.tampilkan_isi_rak()