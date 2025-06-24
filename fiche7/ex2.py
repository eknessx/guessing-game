n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

g = n1
p = n2

if n2 > n1:
    g = n2
    p = n1

pgcd = 0
for i in range(p, 0, -1):
    if p % i == 0 and g % i == 0:
        pgcd = i
        print(f"PGCD = {pgcd}")
        break