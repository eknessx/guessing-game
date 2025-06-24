#Faire le code python qui permet d'afficher les fruits qu'on a avec leur priz de kg puis faire le total a payer apres l'achat, et lorsque l'acheteur paye l'argent, il faut lui render le reste en piecces de 50, 20, 10, 5, 1 euros

fruits = ["Apple", "Banana", "Strawberry", "Orange"]
fruitsCost = [1, 1.5, 2, 0.75]

buyList = [0, 0, 0, 0]

x = ""
for i in range(len(fruits)):
    print(str(i + 1) + " - " + fruits[i], fruitsCost[i])

while True:
    x = input(">")
    if x == "buy":
        break
    if int(x) < 5 and int(x) > 0:
        y = int(input(f"How many KG of {fruits[int(x) - 1]}? "))
        buyList[int(x) - 1] = y
    else:
        print("This is not a valid number.")

s = 0
for i in range(len(buyList)):
    print(f"{fruits[i]}: {buyList[i]} KG")
    s += buyList[i] * fruitsCost[i]
print(f"Price: {s}")

x = int(input("How many euros to pay? "))
toReturn = x - s

l2 = [0, 0, 0, 0, 0]
while toReturn > 0:
    if toReturn >= 50:
        l2[0] += 1
        toReturn -= 50
    elif toReturn >= 20:
        l2[1] += 1
        toReturn -= 20
    elif toReturn >= 10:
        l2[2] += 1
        toReturn -= 10
    elif toReturn >= 5:
        l2[3] += 1
        toReturn -= 5
    else:
        l2[4] += 1
        toReturn -= 1

print(f"Euros returned: {l2[0]} 50s, {l2[1]} 20s, {l2[2]} 10s, {l2[3]} 5s, {l2[4]} 1s")


