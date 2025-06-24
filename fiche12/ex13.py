#On donne 2 tuples chacun de 4 elements, on demande d'ajouter les elements de ces 2 tuples 2 a 2 respectivement
#ex: t1 = (10, 5, 9, 7)
#    t2 = (2, 6, 8, 12)
#t3 = (12, 11, 17, 19)

t1 = (10, 5, 9, 7)
t2 = (2, 6, 8, 12)

l = []

for x in range(0, len(t1)):
    l.append(t1[x] + t2[x])

t3 = tuple(l)
print(t3)