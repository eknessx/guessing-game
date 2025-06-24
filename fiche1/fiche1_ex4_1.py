n = int(input("Number of 4 digits: "))
m = n // 1000
r1 = n % 1000
c = r1 // 100
r2 = r1 % 100
d = r2 // 10
u = r2 % 10
print(m, "Milliards", c, "Centaines", d, "Dizaines", u, "Unite")