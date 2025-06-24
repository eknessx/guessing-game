#D'apprer un code python afficher la forme suivant:
#*     selon le nombre d'etoiles demander a lavence
#**
#***
#****
#***
#**
#*

x = int(input("X: "))

for x2 in range(x):
    print((x2 + 1) * "*")

for x2 in range(x-1, 0, -1):
    print(x2 * "*")