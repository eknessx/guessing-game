#Ecrire la fonction python pour afficher une chaine quelconque diagonalement
def diag(st):
    for x in range(len(st)):
        print((" " * x) + st[x])

diag(input("Word: "))