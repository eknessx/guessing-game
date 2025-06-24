#l'utilisateur donne un nb entier positive et le program annonce combien de foix se nb est divisible par 2

x = int(input("Positive number: "))
i = 0

while x % 2 == 0:
    i += 1
    x = x // 2

print(f"Divisible {i} fois")