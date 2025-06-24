i = input("Number of 4 digits: ")

try:
    i = int(i)
except:
    i = "c"

while i == "c" or i < 1000 or i > 9999:
    if i == "c":
        i = input("Invalid, only numbers allowed: ")
    else:
        i = input("Invalid, only 4 digits allowed: ")
    try:
        i = int(i)
    except:
        i = "c"

m = i // 1000
r = i % 1000
c = r // 100
r2 = r % 100
d = r2 // 10
u = r2 % 10

print(m, "Milliers,", c, "Centaines,", d, "Dizaines,", u, "Unites")
