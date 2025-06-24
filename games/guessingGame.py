import random

number = random.randrange(1, 21)

lives = 5

while lives >= 0:
    if lives == 0:
        print(f"You lost! The number is {number}")
        break

    x = int(input("Guess the number: "))

    if x == number:
        print("Correct!")
        break
    elif x < number:
        print("The number is bigger.")
    else:
        print("The number is smaller.")
    
    lives -= 1
    print(f"You have {lives} lives left.")