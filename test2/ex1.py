import random

score = 0
for i in range(10):
    r = random.randrange(1, 11)
    r2 = random.randrange(1, 11)
    print(r, "*", r2)
    n = int(input("Number: "))
    if n == r * r2:
        score += 1
    else:
        score -= 1

print(f"Score: {score}")