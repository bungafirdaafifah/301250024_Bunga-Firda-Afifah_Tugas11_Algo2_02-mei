# Nama Program : Sistem Analisis Log Login Mahasiswa
# NIM : 301250024
# Nama Pembuat : Bunga Firda Afifah
# Tanggal Pembuatan : 11 Juni 2026
# Nama File : 301250024_BungaFirdaAfifah_Tugas11_ParsingData

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def baca_log():
    baris_log = []

    try:
        with open("log.txt", "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    baris_log.append(baris)
    except FileNotFoundError:
        print("File log.txt tidak ditemukan!")
    except OSError as error:
        print(f"Gagal membaca file log: {error}")

    return baris_log


def tambah_log():
    print("\n=== TAMBAH DATA LOG ===")

    tanggal = input("Masukkan tanggal (contoh: 2026-06-11): ").strip()
    user = input("Masukkan nama user: ").strip()
    aktivitas = input("Masukkan aktivitas: ").strip()

    if not tanggal or not user or not aktivitas:
        print("Data tidak boleh kosong!")
        return

    try:
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"{tanggal},{user},{aktivitas}\n")
        print("Data log berhasil ditambahkan.")
    except OSError as error:
        print(f"Gagal menulis data log: {error}")


# =========================
# TAMPILKAN DATA LOG
# =========================
def tampilkan_log():
    print("\n=== DATA LOG MAHASISWA ===")

    data = baca_log()
    if not data:
        print("Belum ada data log.")
        return

    for baris in data:
        print(baris)


# =========================
# HITUNG JUMLAH AKTIVITAS
# =========================
def hitung_aktivitas():
    data_log = baca_log()
    jumlah_aktivitas = len(data_log)

    print("\n=== JUMLAH AKTIVITAS ===")
    print("Total Aktivitas :", jumlah_aktivitas)


# =========================
# HITUNG USER UNIK
# =========================
def hitung_user_unik():
    user_unik = set()

    for baris in baca_log():
        bagian = [bagian.strip() for bagian in baris.split(",")]
        if len(bagian) >= 2:
            user_unik.add(bagian[1])

    print("\n=== USER UNIK ===")

    for user in sorted(user_unik):
        print(user)

    print("\nJumlah User Unik :", len(user_unik))


# =========================
# ANALISIS LENGKAP
# =========================
def analisis_log():
    jumlah_aktivitas = 0
    user_unik = set()

    for baris in baca_log():
        bagian = [bagian.strip() for bagian in baris.split(",")]
        if len(bagian) >= 2:
            jumlah_aktivitas += 1
            user_unik.add(bagian[1])

    print("\n=== HASIL ANALISIS LOG ===")
    print("Jumlah Aktivitas :", jumlah_aktivitas)
    print("Jumlah User Unik :", len(user_unik))

    print("\nDaftar User Unik :")
    for user in sorted(user_unik):
        print(user)


# =========================
# MENU
# =========================
def menu():
    while True:
        clear()

        print("=== SISTEM ANALISIS LOG LOGIN MAHASISWA ===")
        print("NIM : 301250024")
        print("Nama Pembuat : Bunga Firda Afifah")
        print("Tanggal Pembuatan : 11 Juni 2026")
        print("Nama File : 301250024_BungaFirdaAfifah_Tugas11_ParsingData")

        print("\n=== MENU ===")
        print("1. Tampilkan Data Log")
        print("2. Hitung Jumlah Aktivitas")
        print("3. Hitung User Unik")
        print("4. Analisis Lengkap")
        print("5. Tambah Data Log")
        print("6. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tampilkan_log()
        elif pilih == "2":
            hitung_aktivitas()
        elif pilih == "3":
            hitung_user_unik()
        elif pilih == "4":
            analisis_log()
        elif pilih == "5":
            tambah_log()
        elif pilih == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia!")

        input("\nTekan Enter untuk melanjutkan...")


# =========================
# PROGRAM UTAMA
# =========================
menu()