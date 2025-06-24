import random
points = 0
for x in range(20):
    player = int(input("number: "))
    f = random.randrange(1,20)
    f2= random.randrange(1,20)
    if player == f*f2:
        points +=1
    else:
        points -=1
print(f"your current points is :{points}")