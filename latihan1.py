print("Program bilangan pendeteksi ganjil/genap")
bil = int(input("Masukan angka : " ))
if (bil < 0 ) :
    print("Masukan bilangan positif")
else:
    if (bil%2 == 0) :
        print("{0} adalah bilangan genap".format(bil))
    else:
        print("{0} adalah bilangan ganjil".format(bil))