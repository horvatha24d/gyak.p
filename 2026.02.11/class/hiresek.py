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


class állat:
    def __init__(self,nev,testomeg):
        self.nev=nev
        self.tetomeg=testomeg


for i in range(3):
    nev=input("Add meg egy állat nevét:")
    testomeg=input("Add meg a testomegét:")
    allat=állat(nev,testomeg)
    vege=f"{allat.nev} {int(allat.tetomeg)}"
    f=open("2026.02.11/állatok.txt","w").write(vege)
    f.close()
