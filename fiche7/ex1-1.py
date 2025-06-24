n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

g = n1
p = n2

if n2 > n1:
    g = n2
    p = n1

ppcm = 0
for i in range(1, p + 1):
    m = g * i
    if m % p == 0:
        ppcm = m
        print(f"PPCM = {ppcm}")
        break