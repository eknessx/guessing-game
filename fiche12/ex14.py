#On donne 2 tuples tu1 et tu2 on demande de multiplier tous les elements de tu1 par tous les elements de tu2 respectivement
tu1 = (10, 9, 5)
tu2 = (2, 3, 4, 5, 6)

for x in tu1:
    for y in tu2:
        print(f"{x} * {y} = {x * y}")