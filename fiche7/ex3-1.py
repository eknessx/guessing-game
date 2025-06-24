c = 0
nb = int(input("nombre entier: "))

while nb // 2 >= 1:
    c += 1
    nb = nb // 2
    
print(c)