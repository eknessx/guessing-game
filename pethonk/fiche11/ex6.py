lcolor = ["Red", "Green", "Blue", "Brown","Black","White","Brown"]
lcolor2=["Brown","Pink","blue","Black"]
def color(l1,l2):
    listr=[]
    for x in l1:
        if not x in l2:
            listr.append(x)
    return listr
print(color(lcolor,lcolor2))