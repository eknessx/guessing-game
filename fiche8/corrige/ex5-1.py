x = int(input("Nombre 1: "))
y = int(input("Nombre 2: "))

while x != y and x + y != 5 and abs(x - y) != 5:
    x = int(input("Nombre 1: "))
    y = int(input("Nombre 2: "))
print("Vrai")