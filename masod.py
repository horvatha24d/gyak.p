szam=int(input("Adjon meg egy számot:"))
oszthatoharom=szam% 3 ==0
oszthatoöt= szam % 5 == 0

if oszthatoharom and oszthatoöt:
    print("a szám osztható harommal és öttel is")
elif oszthatoharom:
    print("A szám osztható hárommal,de öttel nem")
elif oszthatoöt:
    print("A szám osztható öttel, de hárommal nem")
else:
    print("A szám nem osztható hárommal,és öttel sem")