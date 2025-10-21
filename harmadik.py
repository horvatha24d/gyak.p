szam1=float(input("Adja meg az elsö számot:"))
szam2=float(input("Adja meg a második számot:"))
szam3=float(input("Adja meg a harmadik számot:"))
if szam1   <=szam2 and szam1<= szam3:
    if szam2<=szam3:
      print(f"A számok növekvő sorrendben: {szam1},{szam2},{szam3}")
    else:
      print(f"A számok növekvő sorrrendben:{szam1},{szam3},{szam2}")
elif szam2 <=szam1 and szam2<=szam3:
   if szam1<=szam3:
      print(f"A számok növekvő sorrendben: {szam2},{szam1},{szam3}")
   else:
      print(f"A számok növekvő sorrendben:{szam2},{szam3},{szam1}")
else:
   if szam1<=szam2:
      print(f"A számok növekvő sorrendben: { szam3},{szam1},{szam2}")
   else:
      print(f"A számok növekvő sorrendben: {szam3}.{szam2},{szam1}")

