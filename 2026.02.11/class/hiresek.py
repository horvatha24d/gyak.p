from hiresek_alap import HíresNő

hiresek = []

for i in range(3):
    név = input("Add meg egy híres nő nevét! ")
    foglalkozás = input("Add meg a foglalkozását! ")
    nemzetiség = input("Add meg a nemzetiségét (a/n)! ")

    nő = HíresNő(név, foglalkozás, nemzetiség)
    hiresek.append(nő)

for nő in hiresek:
    print(f"{nő.előtag()} {nő.név} egy híres {nő.foglalkozás}")

