#Ecrire le code python qui affiche true si 2 listes donnees ayant 1 element au moins communs false dans le cas contraire
l1 = ["123", "word", "Python", "liste"]
l2 = ["pop", "123", "sans", "rima", "amanda", "jason", "1221", "majd", "dd"]
l3 = []

found = False
for x in l1:
    if x in l2:
        found = True
        l3.append(x)  

print(found)
print(l3)