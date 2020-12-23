print("Program penampil bilangan ganjil")
b1 = int(input("masukan batas bawah : "))
b2 = int(input("masukan batas atas : "))
if (b1%2 == 0 ) :
    print("Masukan bilangan ganjil")
else:
    if (b1%2 == 1) :
        for a in range (b1,b2+1):
            if (a%2 != 0): 
                print(a,end=" ")