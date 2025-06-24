#l'utilisater donne un entier et le programme affiche pair s'il est divisible par 2, et impair dans le cas contrair
a = int(input("Number: "))
reste = a % 2
if reste == 0:
    print("Pair")
else:
    print("Impair")