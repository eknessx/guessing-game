import random
points = 0
for x in range(5):
    f = random.randrange(1,5)
    f2= random.randrange(1,10)
    print(f, "*" ,f2)
    player = int(input("number: "))
    if player == f*f2:
        points +=1
        print("true")
    else:
        points -=1
        print("false")
print(f"your current points is :{points}")
