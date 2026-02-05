'''adat=open("homerseklet.txt","r",encoding="UTF-8")

homer=[]
for sor in adat:
    homer.append(float(sor.strip()))

adat.close()


napok=len(homer)
print("Napok szama",napok)


atlag=sum(homer)/napok
print("Atlag hő:",atlag)


min=min(homer)
leghnp=homer.index(min)+1

print("Leghnp:",leghnp,min,"C")'''


##

'''fajl=open("homerseklet.txt","r")


tart=fajl.read()
Lista=tart.split()

for i in range(len(Lista)):
    Lista[i]=float(Lista[i])

print(Lista)
print("Napok szama:",len(Lista))   
print("Atlaghő:",round(sum(Lista)/len(Lista)))
print("Leghidegebb nap:",Lista.index(min(Lista))+1)'''



import random

# Műveletek szimbólumai
muveletek = {
    '+': 'összeadás',
    '-': 'kivonás',
    '*': 'szorzás',
    '/': 'osztás'
}



# Művelet bekérése
'''while True:
    muvelet_input = input("Melyik műveletet gyakorlod? (+, -, *, /): ").strip()
    if muvelet_input in muveletek:
        break
    print("Kérlek, csak +, -, * vagy / jelet adj meg!")

# Feladatok számának bekérése
while True:
    try:
        feladat_szam = int(input(f"Hány feladatot szeretnél a {muveletek[muvelet_input]} gyakorlásához? "))
        if feladat_szam > 0:
            break
        print("Kérlek, pozitív számot adj meg!")
    except ValueError:
        print("Kérlek, számot adj meg!")

# Fájl megnyitása írásra
fajl = open("feladat.txt", "w", encoding="utf-8")
fajl.write(f" {muveletek[muvelet_input]} gyakorló feladatlap ({feladat_szam} feladat) \n\n")

for i in range(1, feladat_szam + 1):
    if muvelet_input == '+':
        x, y = random.randint(1, 100), random.randint(1, 100)
    elif muvelet_input == '-':
        x, y = random.randint(10, 100), random.randint(1, x)
    elif muvelet_input == '*':
        x, y = random.randint(1, 12), random.randint(1, 12)
    elif muvelet_input == '/':
        # Egész osztás biztosítása
        osztok = [i for i in range(2, 13) for j in range(1, 13) if i % j == 0]
        x, y = random.choice(osztok), random.randint(1, 12)
    
    fajl.write(f"{i}. {x} {muvelet_input} {y} = \n")

# Fájl bezárása
fajl.close()

print(f"\n Kész! {feladat_szam} {muveletek[muvelet_input]} feladat elkészült a 'feladat.txt' fájlban!")
print("Nyisd meg a fájlt és kezdheted a gyakorlást! ")'''



##

import random

fajl=open('gj.txt','w',encoding='UTF-8')
jel=input('mie:')
db=int(input('db'))

if(jel=='+'):
    for i in range(db):
        szam1=random.randint(1,100)
        szam2=random.randint(1,100)
        fajl.write(str(szam1)+'+'+str(szam2)+'-'+'\n')
elif (jel=='-'):
     for i in range(db):
        szam1=random.randint(1,100)
        szam2=random.randint(1,100)
        fajl.write(str(szam1)+'-'+str(szam2)+'-'+'\n')
elif(jel=='*'):
     for i in range(db):
        szam1=random.randint(1,10)
        szam2=random.randint(1,10)
        fajl.write(str(szam1)+'*'+str(szam2)+'-'+'\n')
elif(jel=='/'):
     for i in range(db):
        szam1=random.randint(1,100)
        szam2=random.randint(1,100)
        fajl.write(str(szam1)+'/'+str(szam2)+'-'+'\n')
     else:
         print('hiba')


















