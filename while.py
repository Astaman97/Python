selesai = False

while not selesai:
    angka=int(input("Masukan angka : "))
    if (angka%2 == 0):
        print("genap")
    else:
        print("Ganjil")
    lanjut = input("lagi ? (ya/tidak) : ")
    if lanjut == "tidak" :
        selesai=True