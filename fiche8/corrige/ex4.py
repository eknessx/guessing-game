n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

s = n1 + n2 + n3
if n1 == n2 or n1 == n3 or n2 == n3:
    s = 0
print(f"La somme est {s}")