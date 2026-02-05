import random

fajl =open('j/adat.txt','r',encoding='UTF-8')

tart=fajl.read()
Lista=(tart.split())

for i in range(len(Lista)):
    Lista[i]=int(Lista[i])
 
print(Lista)


fajl.close()



