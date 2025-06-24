g=int(input("enter number "))
number=[]
for x in range(g):
    m=int(input(f"value {x+1} "))
    number.append(m)
value=int(input())
if value in number:
    print('elle no se trouve pas dans' , number.index(value))
else:
    print('no')