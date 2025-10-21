a= float(input("Adja meg az elsö oldalt:"))
b=float(input("Adja meg a máodik oldalt:"))
c=float(input("Adja meg a harmadik oldalt:"))
if a> 0 and b > 0 and c > 0 and a< b + c and b < a+c and c<a+b:
    print("Igen ezekböl szerkezthető háromszög")
else:
    print("Nem,ezekböl nem szerkezthet háromszőg")