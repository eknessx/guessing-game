#L'utilisateur donne un nb entier et le code affiche si ce nb est premier ou no
x = int(input("Number: "))

prime = True
for i in range(2, x):
    if x % i == 0:
        print("Not prime number.")
        prime = False
        break

if prime:
    print("Prime number.")