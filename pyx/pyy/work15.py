def sort():
    lest=[]
    dup_list=["q","b","e","s","a","a"]
    for i in dup_list:
        if i not in lest:
            lest.append(i)
    return lest
sort()
print(sort())


