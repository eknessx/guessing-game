#Ecrire la function python qui permet de concatener les elements d'une liste dans une chaine
#ex: l = [1,2,3,4,5]
l = [1, 2, 3, 4, 5]

def concat(l):
    s = ""
    for x in l:
        s += str(x)
    return s

print(concat(l))