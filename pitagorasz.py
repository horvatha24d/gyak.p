#enyém


'''a=float(input("Adja meg az egyik befogó hosszát: "))
b=float(input("Adja meg a másik befogó hosszát: "))
c=(a**2+b**2)**0.5
print("A háromszög átfogója:", round(c, 2))'''


#orai
'''
import math
a=float(input("Adja meg az egyik befogó hosszát: "))
b=float(input("Adja meg a másik befogó hosszát: "))
c=math.sqrt(a**2+b**2)
print("A háromszög átfogója:", round(c, 2))'''

#termék árának csökkenése/enyém
'''
x=float(input("Adja meg a termék árát: "))
y=float(input("Adja meg hogy hány százalékkal csökkent az ár: "))
z=x*(1-y/100)
print("A termék új ára:", round(z, 2))'''

#termék árának csökkenése/orai
'''ar=int(input("Adja meg a termék árát: "))
csokk=int(input("Adja meg hogy hány százalékkal csökkent az ár: "))
uj=ar-((csokk/100)*ar)
print("A termék új ára:", round(uj, 2))'''