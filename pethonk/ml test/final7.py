bt1dev=["charbel2","celine","charbel","elia","majd"]
l=len(bt1dev)
for x in range(l):
    print(x,bt1dev[x])
v=bt1dev[0]
bt1dev[0]=bt1dev[l-1]
bt1dev[l-1]=v
print(bt1dev)
