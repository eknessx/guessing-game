wee=["gason","123","pop","aans","1221","pep","majd","rimma"]
c=0
for x in wee:
    if len(x) >=3 and x[0]==x[-1]:
        print(x)
        c+=1
print(c)