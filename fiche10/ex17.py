#Multiplier tout les valeurs d'une liste entree

l = []
n2 = int(input("Length: "))
m = 1
for x in range(n2):
    n = int(input(f"Num {x+1}: "))
    l.append(n)
    m *= n

print(f"Multiplication of {l} is {m}")