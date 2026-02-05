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

fajl=open("homerseklet.txt","r")


tart=fajl.read()
Lista=tart.split()

for i in range(len(Lista)):
    Lista[i]=float(Lista[i])

print(Lista)
print("Napok szama:",len(Lista))   
print("Atlaghő:",round(sum(Lista)/len(Lista)))
print("Leghidegebb nap:",Lista.index(min(Lista))+1)

                 