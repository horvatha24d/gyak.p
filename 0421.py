class auto:
    def __init__(self, tipus, szín, ár):
        self.tipus = tipus
        self.szín = szín
        self.ár = ár

autók = []

for i in range(3):
    tipus=input("Adja meg a típusát:")
    szin=input("Adja meg a színét:")
    ár=int(input("Adja meg az árát:"))
    autók.append(auto(tipus, szin, ár))
for auto in autók:
    print(f"Típus: {auto.tipus}, Szín: {auto.szín}, Ár: {auto.ár}")

legdragabb=max(autók, key=lambda x: x.ár)
print(f"A legdrágább autó: Típus: {legdragabb.tipus}, Szín: {legdragabb.szín}, Ár: {legdragabb.ár}")
    
    


def keres_szín(szín_keresett):
    találtak = [a for a in autók if a.szín.lower() == szín_keresett.lower()]
    if találtak:
        print(f"{len(találtak)} autó található {szín_keresett} színben:")
        for a in találtak:
            print(f"- {a.tipus}: {a.ár} Ft")
        return találtak
    else:
        print(f"Nincs {szín_keresett} színű autó.")
        return []


keresett_szín = input("\nKeresett szín: ")
keres_szín(keresett_szín)




osszes_érték = sum(a.ár for a in autók)
print(f"A kereskedésben lévő autók összértéke: {osszes_érték:,} Ft")
  

print("Fájl létrehozva: draga_erteke.txt")


fajl=open("draga.txt","w" ,encoding='utf-8')    
fajl.write(f"A legdrágább autó: Típus: {legdragabb.tipus}, Szín: {legdragabb.szín}, Ár: {legdragabb.ár}\n")
fajl.write(f"A kereskedésben lévő autók összértéke: {osszes_érték:,} Ft\n")


fajl.close()


