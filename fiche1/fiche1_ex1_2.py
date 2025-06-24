a = int(input("Number: "))
reste = a % 5
if reste == 0:
    print("Divisible par 5")
else:
    print("Pas divisible par 5")
print("Le reste", reste)