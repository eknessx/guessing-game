#creer un code Python qui permet d'entree 2 variables a et b, et d'afficher l'aquelle parmi ces 2 est la plus grand
a = int(input("Number A: "))
b = int(input("Number B: "))

if a > b:
    print("A est plus grand que B")
elif a < b:
    print("B est plus grand que A")
else:
    print("A est equal a B")