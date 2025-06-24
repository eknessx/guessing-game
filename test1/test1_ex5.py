n = int(input("Number: "))

m = n // 1000
r = n % 1000
c = r // 100
r2 = r % 100
d = r2 // 10
u = r2 % 10

print(m, "milliers", c, "centaines", d, "dizaines", u, "unites")