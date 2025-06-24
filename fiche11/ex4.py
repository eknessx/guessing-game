#Avec une fonction python cree un histogramme apartir d'une liste donner entree
#liste_donnee = [1, 2, 3, 4, 5]
#ca veut dire afficher l'histogramme former de
#*
#**
#***
#****
#*****

liste_donnee = []

def histogramme(l):
    for x in l:
        print("*" * x)

for x in range(5):
    y = int(input(f"Number {x + 1}: "))
    liste_donnee.append(y)

histogramme(liste_donnee)