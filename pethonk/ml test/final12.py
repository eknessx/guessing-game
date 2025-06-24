m=1
g=int(input("enter value of a list"))
this_list = []
for x in range(g):
    v=int(input(f"enter value of g{x+1}"))
    this_list.append(x)
    m*=v
print(this_list,"multiplicstion of all elements is",m) 
