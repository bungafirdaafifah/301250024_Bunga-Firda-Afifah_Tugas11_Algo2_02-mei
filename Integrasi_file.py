# Nama Program : Integrasi Mini Sistem Dictionary & File
# Nim : 301250024
# Nama Pembuat : Bunga Firda Afifah
# Tanggal pembuatan : 11 Juni 2026
# Nama file : 301250024_BungaFirdaAfifah_Tugas_Algo2_IntegrasiFile

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# =========================
# DICTIONARY
# =========================
data = {
    "A01": 34,
    "A02": 12,
    "A03": 7,
    "A04": 23,
    "A05": 56,
    "A06": 89,
    "A07": 11,
    "A08": 67,
    "A09": 34,
    "A10": 90,
    "A11": 90,
}

# Set untuk menyimpan kode unik
data_unik = set(data.keys())

# =========================
# SIMPAN DATA KE FILE
# =========================
def simpan_file():

    with open("data.txt", "w") as file:
        file.write("Data Awal\n")  # Bersihkan isi file sebelum menulis ulang

        for kode, nilai in data.items():

            file.write(f"{kode},{nilai}\n")

    print("Data juga disimpan ke file 'data.txt'")

# =========================
# BACA DATA DARI FILE
# =========================
def baca_file():

    global data
    global data_unik

    try:

        with open("data.txt", "r") as file:

            data.clear()

            for baris in file:
                baris_bersih = baris.strip()

                if not baris_bersih:
                    continue

                if baris_bersih in {"Data Awal", "Data Setelah Sorting", "Hasil Pencarian"}:
                    continue

                if "," not in baris_bersih:
                    continue

                kode, nilai = baris_bersih.split(",", 1)
                data[kode] = int(nilai)

        data_unik = set(data.keys())

    except FileNotFoundError:

        # Jika file belum ada,
        # buat file dari data dictionary awal
        simpan_file()

# =========================
# TAMPILKAN DATA
# =========================
def tampilkan():

    print("\n=== DATA SEBELUM SET ===")

    if not data:
        print("Data kosong!")
        return

    for kode, nilai in data.items():
        print(f"{kode} : {nilai}")

    print("\n=== DATA SAAT INI ===")

    seen = set()

    for kode, nilai in data.items():

        if nilai not in seen:

            print(f"{kode} : {nilai}")

            seen.add(nilai)

# =========================
# INPUT DATA
# =========================
def tambah_data():

    global data
    global data_unik

    kode = input("Masukkan kode data : ")

    if kode in data_unik:
        print("Kode data sudah ada!")
        return

    try:
        nilai = int(input("Masukkan nilai : "))

    except ValueError:
        print("Nilai harus berupa angka!")
        return

    data[kode] = nilai
    data_unik.add(kode)

    # Simpan ke file
    simpan_file()

    print("Data berhasil ditambahkan!")
    print("Data juga disimpan ke file 'data.txt'")

# =========================
# SORTING DATA
# =========================
def sorting_data():

    if not data:
        print("Data kosong!")
        return

    hasil_sort = sorted(
        data.items(),
        key=lambda item: item[1]
    )

    print("\n=== DATA SETELAH SORTING ===")

    for kode, nilai in hasil_sort:
        print(f"{kode} : {nilai}")
    with open("data.txt", "w") as file:
        file.write("Data Setelah Sorting\n")  # Bersihkan isi file sebelum menulis ulang
        for kode, nilai in hasil_sort:
            file.write(f"{kode},{nilai}\n")
    print("Hasil sorting juga disimpan ke file 'data.txt'")
# =========================
# SEARCHING DATA
# =========================
def cari_data():

    if not data:
        print("Data kosong!")
        return

    kode = input("Masukkan kode yang dicari : ")

    if kode in data:

        print("\nData ditemukan")
        print(f"{kode} : {data[kode]}")

        with open("data.txt", "w") as file:
            file.write("Hasil Pencarian\n")  # Bersihkan isi file sebelum menulis ulang
            file.write(f"{kode},{data[kode]}\n")
        print("Data juga disimpan ke file 'data.txt'")
    else:

        print("Data tidak ditemukan")

# =========================
# MENU
# =========================
def menu():

    while True:

        clear()

        print("=== Integrasi Mini Sistem Dictionary & File ===")
        print("NIM : 301250024")
        print("Nama Pembuat : Bunga Firda Afifah")
        print("Tanggal Pembuatan : 11 Juni 2026")

        print("\n=== MENU ===")
        print("1. Input Data")
        print("2. Tampilkan Data")
        print("3. Sorting Data")
        print("4. Searching Data")
        print("5. Keluar")

        pilih = input("Pilih menu : ")

        if pilih == "1":

            tambah_data()

        elif pilih == "2":

            tampilkan()

        elif pilih == "3":

            sorting_data()

        elif pilih == "4":

            cari_data()

        elif pilih == "5":

            print("Program selesai.")
            break

        else:

            print("Pilihan tidak tersedia!")

        input("\nTekan Enter untuk melanjutkan...")

# =========================
# PROGRAM UTAMA
# =========================
baca_file()
menu()