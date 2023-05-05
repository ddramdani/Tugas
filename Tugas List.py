# Membuat fungsi list untuk data buku.

list_buku = []
# while adalah syntax yang digunakan untuk eksekusi perulangan selama ekspresi benar.
# True tipe data boolean
while True:
    print(f"Masukan Data Buku")
    #fungsi input() digunakan untuk membaca inputan dari user.
    # \t adalah tab
    # \n adalah baris baru
    judul = input("Judul Buku\t : ")
    penulis = input("Nama Penulis\t : ")
    tahun_terbit = input("Tahun Terbit\t : ")
    penerbit = input("Penerbit\t : ") 

    data_buku = [judul,penulis,tahun_terbit,penerbit]
    # fungsi append berfungsi untuk menambahkan nilai array pada urutan terakhir
    list_buku.append(data_buku)

    print("\n","="*10,"Data Buku","="*10)
    # looping for
    # enumerate() adalah fungsi yang digunakan untuk mengembalikan panjang iterable dan mengulang itemnya secara bersamaan.
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]} | {buku[2]} | {buku[3]}")

    print("\n","="*31)
    lanjut = input("Masukan Data Buku?(y/n)")
    # kondisi if
    if lanjut == "n":
        break

print("PROGRAM SELESAI")  