#Ecrire le code python pour creer tout les chaines possibles en utilisant "a", "o", "e", "i", "u", utiliser chacun une seule fois
#dans le mot
import random

l = ["a", "o", "e", "i", "u"]
for i in range(5):
    random.shuffle(l)
    print("".join(l), end=" ")