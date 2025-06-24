x = float(input("Number: "))
n = x * 100
r = n % 100
n2 = n // 100

if r >= 50:
    print(n2 + 1)
else:
    print(n2)