#Faire la table de muliplication du nb entree (1->10)
x = int(input("Number: "))

for i in range(1, 11):
    m = x * i
    print(f"{x}x{i}={m}")