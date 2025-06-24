tuple1=(1,5,9,14)
tuple2=(2,6,7,11)
tuple3=[]


for x in range(0,len(tuple1)): 
    s=tuple1[x]+tuple2[x]
    print(s)
    tuple3.append(s)
    print(tuple3)

