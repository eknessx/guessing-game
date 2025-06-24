k=int(input("entier positify"))
n=int(input("nbr de fois"))



def calc(k,n):
    cube=k**3
    x=1
    while x<=n:
        cube+=cube
        x+=1
    return cube
print(calc(k,n))