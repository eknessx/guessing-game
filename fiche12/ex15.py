a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

v = [0, 0, 0]
v[0] = a

if b > a:
    v[1] = a
    v[0] = b
if c > a:
    v[1] = a
    v[0] = c

print(v[2], v[1], v[0])