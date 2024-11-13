# Meminta input berat badan (dalam kilogram) dan tinggi badan (dalam meter)
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

# Menghitung BMI
bmi = berat_badan / (tinggi_badan ** 2)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 24.9:
    kategori = "Berat badan normal"
elif 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
else:
    kategori = "Obesitas"

# Menampilkan hasil BMI dan rekomendasi
print(f"Indeks Massa Tubuh (BMI) Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")
