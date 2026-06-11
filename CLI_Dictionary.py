#Nama Program : Mini Sistem CLI Dictionary
#Nim : 301250024
#Nama Pembuat : Bunga Firda Afifah
#Tanggal pembuatan : 07 Juni 2026
#Nama file : 301250024_BungaFirdaAfifah_Tugas_Algo2_07-06-2026

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary
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

# Set untuk menyimpan kode yang unik
data_unik = set(data.keys())

# =========================
# TAMPILKAN DATA
# =========================
def tampilkan():
    print("\n=== DATA SEBELUM SET===")
    if not data:
        print("Data kosong!")
        return
    
    for kode, nilai in data.items():
        print(f"{kode} : {nilai}")

    print("\n=== DATA SAAT INI ===")

    if not data:
        print("Data kosong!")
        return
    
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

    kode = input("Masukkan kode data : ")

    if kode in data_unik:
        print("Kode data sudah ada!")
        return

    nilai = int(input("Masukkan nilai : "))

    data[kode] = nilai
    data_unik.add(kode)

    print("Data berhasil ditambahkan!")

# =========================
# SORTING DATA
# =========================
def sorting_data():

    if not data:
        print("Data kosong!")
        return

    hasil_sort = sorted(data.items(), key=lambda item: item[1])

    print("\n=== DATA SETELAH SORTING ===")

    for kode, nilai in hasil_sort:
        print(f"{kode} : {nilai}")

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
    else:
        print("Data tidak ditemukan")

# =========================
# MENU
# =========================
def menu():

    while True:

        clear()

        print("=== Integrasi Mini Sistem Dictionary ===")
        print("NIM : 301250024")
        print("Nama Pembuat : Bunga Firda Afifah")
        print("Tanggal Pembuatan : 07 Juni 2026")

        print("\n=== MENU ===")
        print("1. Input")
        print("2. Tampilkan")
        print("3. Sorting")
        print("4. Searching")
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

menu()
