'''from hiresek_alap import HíresNő

hiresek = []

for i in range(3):
    név = input("Add meg egy híres nő nevét! ")
    foglalkozás = input("Add meg a foglalkozását! ")
    nemzetiség = input("Add meg a nemzetiségét (a/n)! ")

    nő = HíresNő(név, foglalkozás, nemzetiség)
    hiresek.append(nő)

for nő in hiresek:
    print(f"{nő.előtag()} {nő.név} egy híres {nő.foglalkozás}")'''


'''class HíresNő:
    def __init__(self, név, foglalkozás, nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség

    def elötag(self):
        if self.nemzetiség == "a":
            return "Ms."
        else:
            return 'Frau'


#----------------------------------------------------------#
hiresnok=[]
for i in range(3):
    nev=input("Add meg egy hires no nevet:")
    foglalkozas=input("Add meg a foglalkozasat:")
    nemzetiseg=input("Add meg a nemzetiseget (a/n):")
    hiresno=HíresNő(nev,foglalkozas,nemzetiseg)
    hiresnok.append(hiresno)

for elem in hiresnok:
    print(elem.elötag(), elem.név, elem.foglalkozás)'''


'''class állat:
    def __init__(self,nev,testomeg):
        self.nev=nev
        self.tetomeg=testomeg

tomegek=[]
for i in range(3):
    nev=input("Add meg egy állat nevét:")
    testomeg=input("Add meg a testomegét:")
    allat=állat(nev,testomeg)
    vege=f"{allat.nev} {int(allat.tetomeg)}"
    f=open("2026.02.11/állatok.txt","w").write(vege)
    f.close()'''



class Allatok:
    def __init__(self,nev,testomeg):
        self.nev=nev
        self.testomeg=testomeg

allat=[]
for i in range(3):
    nev=input("Add meg egy állat nevét:")
    testomeg=input("Add meg a testomegét:")
    pallat=Allatok(nev,testomeg)
    allat.append(pallat)


#legnehezebb állat
legn=allat[0]
for pallat in allat:
    if (int(pallat.testomeg)>int(legn.testomeg)):
        legn=pallat
        '''suly=open("állatok.txt","w",encoding="UTF-8")
        suly.write(f"A legnehezebb állat: {legn.nev} {legn.testomeg}")
        suly.close()'''

f=open("2026.02.11/állatok.txt","w",encoding="UTF-8")
f.write(f"A legnehezebb állat: {legn.nev} {legn.testomeg}")
f.close()