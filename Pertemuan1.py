# Struktur Data
# List dan Dictionary

jumlah = int(input("Masukkan jumlah mahasiswa: "))

mahasiswa = []  # List [] untuk menyimpan data mahasiswa

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)
    nama = input("Nama: ")
    nilai = int(input("Nilai: "))

    data = {
        "nama": nama,
        "nilai": nilai
    }  # Dictionary data = {}

    mahasiswa.append(data)  # Simpan ke dalam list

print("\n=== Data Mahasiswa ===")
for m in mahasiswa:
    print("Nama:", m["nama"], "- Nilai:", m["nilai"])