# SHALOMMITA PRANATANTRI
# 71200640
# LAB-08-MEMBUKA DAN MENULIS FILE TXT DI PYTHON

# INPUT
# Nama File, Nama Lengkap, Tempat dan Tanggal lahir, pilihan hobi, hobi

# PROSES
# Membuka dan menulis file txt
# Melakukan perulangan untuk hobi sesuai dengan pilihannya

# OUTPUT
# File txt berisikan biodata yang sudah dituliskan/diinputkan oleh user

def utama():
    try:
        inp=input("Masukkan file yang akan dibuka: ")
        if inp=="biodata.txt":
            file=open("D:\Bahan Lab08\\biodata.txt","w")
            nama=input("Nama Anda: ")
            tempat=input("Tempat lahir: ")
            tanggal=int(input("Tanggal lahir: "))
            pilihan=int(input("Berapa hobi Anda? "))
            hobi2=""
            if pilihan>=2:
                for i in range(pilihan):
                    hobi=input("Hobi Anda: ")
                    hobi2+=hobi+"  "
            else:
                hobi=input("Hobi Anda: ")
            file.write("Nama Lengkap: "+nama+"\n")
            file.write("Tempat lahir: "+tempat+"\n")
            file.write("Tanggal lahir: "+str(tanggal)+"\n")
            file.write("Hobi Anda: "+hobi2+"\n")
            file.close()
    except:
        print("Ada kesalahan")

utama()