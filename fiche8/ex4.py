n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

s = 0
if (n1 == n2 or n2 == n3 or n1 == n3) == False:
    s = n1 + n2 + n3

print(f"s={s}")