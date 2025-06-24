n1=int(input())
n2=int(input())
if n1>n2:
    g=n1
    p=n2
else:
    g=n2
    p=n1
for x in range(p,0,-1):
    if g%x==0 and p%x==0:
        print(f"le pgcd est {x}")
        break