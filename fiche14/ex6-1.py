#Faire le code python qui permet d'afficher les fruits qu'on a avec leur priz de kg puis faire le total a payer apres l'achat, et lorsque l'acheteur paye l'argent, il faut lui render le reste en piecces de 50, 20, 10, 5, 1 euros
fruits = ["Apple", "Banana", "Strawberry", "Orange"]
costs = [1, 2, 4, 8]
bought = [0, 0, 0, 0]

while True:
    for x in range(len(fruits)):
        print(f"{x+1}-{fruits[x]}, {costs[x]} per kg")
    ch = int(input("Choice: "))

    if ch == 0:
        break
    else:
        y = int(input("How many? "))
        bought[ch - 1] += y

total = 0
for x in range(len(fruits)):
    total += bought[x] * costs[x]
print("You should pay", total)

p = int(input("How many will you pay? "))
toReturn = p - total

euros = [50, 20, 10, 5, 1]
for x in euros:
    euro2 = 0
    while toReturn >= x:
        toReturn -= x
        euro2 += 1
    print(f"{euro2} of {x}")