class magassag:
    def __init__(self, nev, cm):
        self.nev = nev
        self.cm = cm

f = open("2026.02.11/class/0219/diak.txt", "r", encoding="utf-8")
adatok = f.read()
f.close()

w=print(adatok)

adatok = adatok.split("\n")
diakok = []
db = 0

for sor in adatok:
    if sor.strip():
        nev, cm = sor.strip().split(";")
        diak = magassag(nev, int(cm))
        diakok.append(diak)
        db += 1

d=print(f"A diákok száma: {db} fő")

# Legmagasabb diák(ok) enumerate nélkül
max_cm = max(diak.cm for diak in diakok)
legmagasabbak = [diak.nev for diak in diakok if diak.cm == max_cm]
x=print(f"Legmagasabb diák: ", end="")
i = 0
while i < len(legmagasabbak):
    if i > 0:
        print(", ", end="")
    print(legmagasabbak[i], end="")
    i += 1
k=print(f" ({max_cm} cm)")  # While ciklusos kiírás [file:1]

# Átlagmagasság


# Legkisebb magasság
min_cm = min(diak.cm for diak in diakok)
n=print(f"Legalacsonyabb: {min_cm} cm")

wfajl = open("2026.02.11/class/0219/eredmenyek.txt", "w", encoding="utf-8")
