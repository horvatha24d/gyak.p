'''for num in range(1,31):
    if num%7 ==0:
     if num%2 ==0:
        print(f"{num}*")
     else:
        print(num)  '''
'''
for num in range(1,51):
    if num%3 == 0 and num%5 ==0:
        print(num)'''


'''negativ_db = 0


for i in range(8):
    szam = int(input(f"{i+1}. szám: "))
    if szam < 0: 
        negativ_db += 1

print("Negatív számok darabszáma:", negativ_db)'''

'''
osszeg_paros = 0                            qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqssdddddddddddddddd
db_paros = 0


for i in range(6):
    szam = int(input(f"{i+1}. szám: "))
    if szam % 2 == 0:  # Ha páros
        osszeg_paros += szam
        db_paros += 1


if db_paros > 0:
    print("A páros számok átlaga:", osszeg_paros / db_paros)
else:
    print("Nem adtál meg páros számot.")'''



'''for n in range(1, 11): 
    print(n**2)'''


'''
szam = int(input("Adj meg egy számot: "))

print(f"A(z) {szam} osztói:")

for i in range(1, szam + 1):
    if szam % i == 0: 
        print(i)'''


'''for szam in range(2, 101):  
    prim = True
    for i in range(2, int(szam**0.5) + 1):
        if szam % i == 0:
            prim = False
            break
    if prim:
        print(szam)
'''
'''
for i in range(1, 20 + 1):
    print(f"{i:2}  {i*i}")'''

'''for i in range(99,0,-1):
    if i % 3 ==0:
        print(i)
'''
'''
N = int(input("Add meg N értékét: "))

for i in range(1, 2*N, 2): 
    print(f"{i}^2 = {i*i}")'''




import wikipedia
cim = input("Adj meg egy témát: ")
try:    
    tartalom = wikipedia.summary(cim, sentences=3)
    print(tartalom)
except wikipedia.exceptions.DisambiguationError as e:
    print("Több találat is van a megadott témára. Kérlek, pontosítsd a keresést.")
except wikipedia.exceptions.PageError:
    print("Nincs találat a megadott témára.")
except Exception as e:
    print("Hiba történt a Wikipedia elérése során:", e)
