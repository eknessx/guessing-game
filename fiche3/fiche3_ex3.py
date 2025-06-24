#ecrire le code python qui permet d'entrer une temperature et qui ensuite envoie l'etat:
#tempe < 0 = solide; tempe >= 0 < 100 = liquid; tempe > 100 = gazeux
t = int(input("Temperature: "))

if t < 0:
    print("Solid")
elif t >= 0 and t <= 100:
    print("Liquid")
else:
    print("Gazeux")