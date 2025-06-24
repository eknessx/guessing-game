l = []
for x in range(5):
    n = int(input(f"Number {x+1}: "))
    l.append(n)
s = sum(l)
print(f"La somme est {s}")
ma = max(l)
mi = min(l)
print(f"Le plus grand est {ma}, le plus petit est {mi}")