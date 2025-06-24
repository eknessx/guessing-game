x = int(input("Number of lines: "))

if x == 3:
    print(x, "Un Triangle")
elif x == 4:
    print(x, "Un Quadrilatere")
elif x == 5:
    print(x, "Un Pentagone")
elif x == 6:
    print(x, "Un Hexagone")
else:
    print("Error; number out of bounds (3 to 6)")