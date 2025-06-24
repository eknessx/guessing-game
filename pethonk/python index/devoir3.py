cc=0
c=0
s=0
x=int(input("donner un nomber "))
while x>0:
    c+=1
    s+=x
    if x>100:
        cc+=1
    x=int(input('donne un nombre pls'))
print(f"le nombre des entiers est:{c},leur some est{s}, nombre de > 100 est{cc}")