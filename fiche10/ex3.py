# accepte le rayon decimale d'1 cercle de l'user et calculer la surface a 2 chiffres apres la virgule, utiliser library math pour
# utiliser pi
import math

r = float(input("Rayon: "))
print(round(math.pi * (r**2), 2))