import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

data = [34, 12, 7, 23, 56, 89, 11, 67, 34, 90,78, 21, 43, 65, 10, 99]


# TAMPILKAN
# =========================
def tampilkan():
    print("Data:", data)

#INPUT DATA
def tambah_data():
    global data
    n = int(input("Berapa data yang ingin ditambahkan? "))

    for i in range(n):
        angka = int(input(f"Data ke-{len(data)+1}: "))
        data.append(angka)

    print("Data berhasil ditambahkan!")

# =========================
# SORTING
# =========================
def bubble_sort():
    global data
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    print("Data sudah diurutkan")

# =========================
# SEARCHING
# =========================
def binary_search(target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def cari_data():
    if not data:
        print("Data kosong!")
        return

    target = int(input("Cari angka: "))
    idx = binary_search(target)

    if idx != -1:
        print("Ditemukan di index", idx)
    else:
        print("Tidak ditemukan")

# =========================
# MENU
# =========================
def menu():
    while True:
        clear()
        print("=== Integrasi Mini Sistem ===")
        print("Nim: ")
        print("Nama Pembuat:")
        print("Tanggal pembuatan: 02 Mei 2026")
        print()
        print("\n=== MENU ===")
        print("1. Input")
        print("2. Tampilkan")
        print("3. Sorting (Bubble)")
        print("4. Searching (Binary)")
        print("5. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampilkan()
        elif pilih == "3":
            bubble_sort()
        elif pilih == "4":
            cari_data()
        elif pilih == "5":
            break
        else:
            print("Salah pilih!")
        input("\nTekan Enter untuk melanjutkan...")

menu()