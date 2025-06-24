#pour une liste donnee, trouver le nb des valeurs negatives et celui des valeurs positives
l = [-3, 1, 5, -6, 7, -1, 2, 4]

#for i in range(5):
#    l.append(int(input(f"Number {i+1}: ")))

p = []
n = []
for x in l:
    if x >= 0:
        p.append(x)
    else:
        n.append(x)

print(f"Number of positives: {len(p)}, Negatives: {len(n)}")
print(f"{p}, {n}")