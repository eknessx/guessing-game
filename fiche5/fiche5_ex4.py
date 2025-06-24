#Faire le factoriel d'un nb donne
#Ex: 6, factoriel == 1*2*3*4*5*6

x = int(input("Number: "))
x2 = 1

for i in range(1, x + 1):
    x2 = x2 * i

print("Le factoriel est", x2)
