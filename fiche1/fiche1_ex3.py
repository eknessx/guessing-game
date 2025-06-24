#trouver si une annee entree est bissextile ou non
y = int(input("Year: "))
if y % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")