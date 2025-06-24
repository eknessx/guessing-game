d={"nom":"dupuis","prenom":"jacque","age":30}

d["nom"]="jacques"
d["prenom"]="depuis"



print(d)
for x in d.keys():
    print(x)

for s in d.values():
    print(s)

print(d.items())

for f in d.values():
    f=list()
    f.sort(d)
    print(f)
    