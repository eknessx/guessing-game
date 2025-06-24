#Afficher les diviseurs d'un nb entre
x = int(input("Number: "))

for i in range(1, x+1):
    if x % i == 0:
        print(i)
