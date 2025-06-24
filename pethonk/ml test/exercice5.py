enter=input("yo wanna play a guesing number game? yes or no: ")
number=50
if enter=="yes":
    print("ok lets play ")
    import random
    number = random.randint(1,100)
    guess = int(input("guess a number 1 to 100 "))
    while guess != number:
        if guess < number:
            print("too low")
            guess = int(input("guess a number 1 to 100 "))
        elif guess > number:
            print("you got it")
            break
        if  guess > number:
             print("too high")
             guess = int(input("guess a number 1 to 100 again "))
    
