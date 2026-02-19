class Diak:
    def __init__(self,nev,magassag):
        self.nev=nev
        self.magassag=magassag


#fálj feldoolgozása


fajl=open("2026.02.11/class/0219/diak.txt","r",encoding="UTF-8")
#soronkent olvasás
tartalom=fajl.read()
Ltartalom=tartalom.split("\n")
LLtartalim=[]
for sor in Ltartalom:
    Ldarabok=sor.split(";")
    nev=Ldarabok[0]
    magassag=int(Ldarabok[1])
    diak=Diak(nev,magassag)
    LLtartalim.append(diak)

#adaatok ellenőrzése
for diak in LLtartalim:
    print(diak.nev, diak.magassag)

#Elso feladat:diakok szama

print("Diákok száma:", len(LLtartalim),"fő")
#Második feladat: legmagasabb   

legmagasabb=LLtartalim[0]
for diak in LLtartalim:
    if diak.magassag>legmagasabb.magassag:
        legmagasabb=diak
print("A legmagasabb diák:", legmagasabb.nev, legmagasabb.magassag,"cm")



#harmadik feladat: rendezés
Lrendzett=sorted(LLtartalim,key=lambda m: m.magassag,reverse=True)
for diak in Lrendzett:
    print(diak.nev, diak.magassag)