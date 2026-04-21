class Auto:
    def __init__(self, szín,tipus,ár):
        self.szín=szín
        self.tipus=tipus
        self.ár=ár

Lautok=[]
for i in range(3):
    tipus=input("Adja meg a típusát:")
    szin=input("Adja meg a színét:")
    ár=int(input("Adja meg az árát:"))
    auto=Auto(szin,tipus,ár)
    Lautok.append(auto)

legdragabb=Lautok[0]
for auto in Lautok:
    if auto.ár>legdragabb.ár:
        legdragabb=auto

f=open("draga_erteke.txt","w",encoding="utf-8")
kir=(legdragabb.szín+legdragabb.tipus+str(legdragabb.ár))   
f.write(kir)
f.close()
szinkeres=input("Adja meg a színt amit keres:")
Lkeres=[]
for auto in Lautok:
    if auto.szín==szinkeres:
        Lkeres.append(auto)
        
if len(Lkeres)==0:
    print("Nincs ilyen színű autó")
else:
    for auto in Lkeres:
        print(auto.tipus,auto.szín,auto.ár)