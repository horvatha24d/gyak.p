'''x=int(input("SZám:"))


for i in range(1,11):
    print(i,"*",x,"=",i*x)'''


'''for szam in range(2,101,2):

    if(szam%5==0):
        print(szam,end=" ")'''

s=input("páros vagy páratlan számokat kérsz:")

if(s=="páros"):
    for i in range(2,101,2):
        print(i,end=" ")
elif(s=="páratlan:"):
    for i in range(1,101,2):
        print(i,end=" ")
else:
    print("Helytelen bemenet:")
        