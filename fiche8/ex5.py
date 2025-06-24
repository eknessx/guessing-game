n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

if abs(n1 - n2) == 5 or n1 + n2 == 5 or n1 == n2:
    print("Vrai")
else:
    print("Faux")