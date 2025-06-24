tup1=(1,2,23,2,4,5,6,23,23,9,10) 
def reapat(l1):
    listr=[]
    for x in l1:
        if l1.count(x) > 1 and x not in listr:
            listr.append(x)
    return listr
print(reapat(tup1))