L=[33,5,11,6,11,5]
def list_count(L,ch):
    count=0
    for num in L:
        if num==ch:
            count=count+1
    return count
m=5
print(list_count(L,m))