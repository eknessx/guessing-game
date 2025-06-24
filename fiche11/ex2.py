#Supprimer une liste de 10 elements les premiere valeur, jusqu'a arriver a une liste vide
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(l) > 0:
    l.pop(0)
    print(l)