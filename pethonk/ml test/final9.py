g=int(input("enter count: "))
x=" * "
for i in range(g+1):
    print((i+1)*x)
g-=1
for i in range(g,0,-1):
    print(i*x)
    
    