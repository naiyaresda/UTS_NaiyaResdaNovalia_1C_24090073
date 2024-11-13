# Meminta input dari pengguna
tahun = int(input("Masukkan tahun: "))

# Mengecek apakah tahun tersebut adalah tahun kabisat
if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
