import random 
score=12
for x in range(20):
    while x < 20:
        dice=random.randrange(1,19)
        player=int(input("number 1,19 "))
        if dice==player:
            score+=dice
        if score>player:
            print(f"to low dice:{player} ")
        elif player>score:
            print(f"to high:{player} ")
        else:
            print(f"you won:{player} ")
            break
        