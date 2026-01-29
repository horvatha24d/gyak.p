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
osszeg_paros = 0                            
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

#fügvények

'''def koszones(a):
    return f'Szia, {a}!'
    #itt kezdődik a main()/fő fuggvény
nev = input('Mi a neved? ')
print(koszones(nev))'''

##
'''
def osszead(szam1, szam2):
    return szam1 + szam2
def kivon(szam1, szam2):
    return szam1 - szam2
def szoroz(szam1, szam2):
    return szam1 * szam2
def oszt(szam1, szam2):
    if szam2 != 0:
        return szam1 / szam2
    else:
        return "Hiba: Nullával való osztás!"

szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg a második számot: "))
muv = input("Add meg a műveletet (+, -, *, /): ")
if muv == '+':
    print(osszead(szam1, szam2))
elif muv == '-':
    print(kivon(szam1, szam2))
elif muv == '*':
    print(szoroz(szam1, szam2))
elif muv == '/':
    print(oszt(szam1, szam2))
else:
    print("Érvénytelen művelet!")
'''

##
'''def szamol(max_szam,elért_pontszám):
    szazalék = (elért_pontszám / max_szam) * 100
    if(szazalék >= 40):
        return str(szazalék)+'%-ra sikerult a dolgozat, sikeres!'
    else:
        return str(szazalék)+'%-ra nem sikerult a dolgozat, sikertelen!'



név=input("Add meg a neved: ")
max_szam = int(input("Add meg a maximum számot: "))
elért_pontszám = float(input("Add meg az elért pontszámot: "))


print(név,szamol(max_szam,elért_pontszám,))'''

                 


##


'''
def feltolt(Rlista):
    for i in range(10):
        Rlista.append(random.randint(0,9))
    return Rlista

def paratlan(paratlandb):
    for szam in Rlista:
        if szam%2 ==1:
            paratlandb +=1
    return paratlandb



def ism(ujjlista):
    for i in Rlista:
        if(i not in ujjlista):
            ujjlista.append(i)
    return ujjlista



def hianyzo(hianyzos):
    for i in range(10):
        if i not in Rlista:
            hianyzos.append(i)
            
    if hianyzos:
        return "Hiányzó számok:",hianyzo(hianyzos)
        
    else:
        return "Nincsenek hiányzó számok."
    






import random

Rlista= []
print(feltolt(Rlista))
paratlandb=0

print(f"A listában {paratlan(paratlandb)} páratlan szám van.")

ujjlista = []

print(ujjlista,ism(ujjlista = []))

hianyzos = []'''

##
'''def ora_perc(percek):
    ora = percek // 60
    perc = percek % 60
    return ora, perc


for i in range(3):
    cim = input(f"{i+1}. film címe: ")
    hossz = int(input("Hossz (percben): "))

    ora, perc = ora_perc(hossz)

    print("A(z) ",cim," hossza:", ora," óra",perc, "perc")
'''
##


def szamol(cím,fperc):
    ora=fperc[i]//60
    perc=fperc[i]%60
    return 'A ',cím[i],ora,"ora és ",perc,"perc"


cím=[]
fperc=[]

for i in range(3):
    fc=input('filmcime:')
    cím.append(fc)
    fp=int(input('hossz(pecben):'))
    fperc.append(fp)

for i in range(3):
    print(szamol(cím,fperc))


    


