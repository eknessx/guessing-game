import random


def guess():
    print("Welcome to the number guessing game!")
    print("I have selected a random number between 1 and 100.")
    print("You have 10 attempts to guess the number.")
    print("Let's begin!")

    numbers = [i for i in range(1, 101)]
    random.shuffle(numbers)
    secret_number = numbers[0]
    attempts = 10
    guessed_numbers = []

    while attempts > 0:
        enter = int(input("enter your guess: "))
        if enter == secret_number:
            print("Congratulations! You've guessed the number!")
            break
        elif enter >= secret_number:
            print("Your guess is too high.")
            attempts -= 1
        elif enter <= secret_number:
            print("print ,Your guess is too low.")
            attempts -= 1
        if attempts == 0:
            print("Sorry, you've used all your attempts. The number was", secret_number)
            break
        guessed_numbers.append(enter)
        print("Guessed numbers:", guessed_numbers)
        print("Attempts remaining:", attempts)
guess()

