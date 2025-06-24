import random

hp = 40
enemyHp = 500
dices = 5000000

diceCounters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def rand():
    return str(random.randrange(1, 1001))

while hp > 0 and enemyHp > 0:
    print("1-Add +2 dice gain to 1")
    x = input("Your choice: ")

    if x == "1":
        diceCounters[1] += 2

    l = []
    ic = 0

    for i in range(dices):
        y = rand()
        l.append(y)
        if ic < 100:
            print(y)
        ic += 1

    totalAdd = 0
    for y in l:
        if int(y) < 6:
            enemyHp -= 1
        for i2 in range(10):
            if y[-1] == str(i2):
                dices += diceCounters[i2]
                totalAdd += diceCounters[i2]

    print(f"You gained {totalAdd} dices!")