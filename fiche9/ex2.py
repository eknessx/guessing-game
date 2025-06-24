#afficher les nbs pair entre deux limites entree
l0 = int(input("Min: "))
l1 = int(input("Max: "))

for i in range(l0, l1 + 1):
    if i % 2 == 0 and i != 0:
        print(i)