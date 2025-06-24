l = []
s = 0
for i in range(0, 5):
    x = int(input(f"Number {i + 1}: "))
    l.append(x)
    s += x

g = max(l)
p = min(l)

print(f"Somme: {s}, Plus grand: {g}, Plus petit: {p}")