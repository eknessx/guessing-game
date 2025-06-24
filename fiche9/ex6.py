#dice from 1 to 6, if == guess, +score, else -score, 10 times
import random

score = 0

for i in range(0, 10):
    r = random.randrange(1, 7)
    print(f"Score: {score}")
    print("The dice was rolled, choose a number from 1 to 6")
    x = int(input("Guess the number: "))
    if x == r:
        print(f"Correct! +{r} score")
        score += r
    else:
        print(f"Incorrect! -{r} score")
        score -= r
        if score < 0:
            score = 0

print(f"Your score: {score}")