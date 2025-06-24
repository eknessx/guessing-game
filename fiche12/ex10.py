#Ecrire une fonction en python pour supprimer un element d'un tuple
def tupleRemove(t, x):
    l = list(t)
    l.remove(x)
    return tuple(l)

def tupleRemoveNoConvert(t, x):
    i = t.index(x)
    t1 = t[:i]
    t2 = t[i + 1:]
    t3 = t1 + t2
    return t3

print(tupleRemove((1, 2, 3), 2))
print(tupleRemoveNoConvert((1, 2, 3), 2))