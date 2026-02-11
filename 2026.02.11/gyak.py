'''fajl=open('2026.02.11/nevek.txt','r',encoding='UTF-8')
import locale 
locale.setlocale(locale.LC_COLLATE,"hu-HU.UTF-8")
tart=fajl.read()
Lnevek=tart.split()
print(Lnevek)


print('Nevek száma:',len(Lnevek),"fő")
print("Nevek ABD sorrendben:",sorted(Lnevek,key=locale.strxfrm))
nev=input("Nev:")

if (nev.lower().capitalize in Lnevek):
    print("A nev benne vn a fajlban")
else:
    print("Nincs ilyne nev a listaban")
'''


###szamok
szamf=open('2026.02.11/szam.txt',"r")


tart=szamf.read()
lszam=tart.split()
print(lszam)

efajl=open("2026.02.11/egesz.txt","w")
wfajl=open("2026.02.11valos.txt","w")
for elem in lszam:
    if("."in elem):
        wfajl.write(elem+" ")
    else:
        efajl.write(elem)

efajl.close()
wfajl.close()