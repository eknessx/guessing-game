#Ecrire la fonction python pour afficher une chaine quelconque diagonalement
def diag(st):
    for x in range(len(st)):
        if x == 0:
            print(" ".join(list(st)))
        else:
            print(st[x] + (" " * x) + st[x])

diag(input("Word: "))