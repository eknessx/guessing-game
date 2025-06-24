lch = ["pop", "123", "sans", "rima", "amanda", "jason", "1221", "majd", "dd"]

y = 0
for x in lch:
    if len(x) > 2 and x[0] == x[-1]:
        print(x)
        y += 1
print(f"Il-y-a {y} mots")