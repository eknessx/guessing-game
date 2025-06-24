#On donne le tuple t
#A-Trouver la longueur de t
#B-Trouver l'indice de cherry
#C-Reverser le tuple
#D-Imprimer un tuple avec un formatage de chaine
t = ("apple", "banana", "cherry", "Jason")
print(len(t))
print(t.index("cherry"))
t = t[::-1]
print(t)
for i in reversed(t):
    print(i, end=" ")
print("")
t2 = (100, 200, 300)
t2 = format(t2)
print(t2)
print(type(t2))