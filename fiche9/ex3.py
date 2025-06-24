#pour un nb decimal a 2 ch apres la virgule on demande de faire l'arondissement de facon que, si apres la virgule >= 50 on ajoute a
#l'unite 1 si non on enleve les chiffres apres la virgule
x = float(input("Number: "))

if x % (x // 1) >= 0.5:
    print(x // 1 + 1)
else:
    print(x // 1)