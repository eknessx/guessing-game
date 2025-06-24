nombres = [1, 12, 21, 4, 15, 6, 7, 10, 9]
cp = 0
ci = 0

for x in nombres:
    if x % 2 == 0:
        cp += 1
    else:
        ci += 1
print("Paires", cp, "Impaires", ci)