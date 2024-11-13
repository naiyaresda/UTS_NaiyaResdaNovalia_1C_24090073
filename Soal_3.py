# Meminta pengguna untuk memasukkan jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# variabel untuk menyimpan total harga
total_harga = 0

# Meminta pengguna untuk memasukkan harga setiap barang dan menambahkannya ke total harga
for i in range(1, jumlah_barang + 1):
    harga = float(input(f"Masukkan harga barang ke-{i}: "))
    total_harga += harga

# Menampilkan total harga belanjaan
print(f"Total harga belanjaan: {total_harga}")
