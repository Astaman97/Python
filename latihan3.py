def hitungTotal(a,b):
    return a*b
def hitungNet(c,d):
    return hitungTotal(c,d)-5000
jumlah = int(input("Jumlah : "))
hargaSatuan = int(input("Harga : "))


if (hitungTotal(jumlah,hargaSatuan) >=50000):
    print(hitungNet(jumlah,hargaSatuan))
else:
    print(hitungTotal(jumlah,hargaSatuan))