#the code is based on a number guessing game very simple the only diff is the code can give you the possible rage of the guess like 1 around 67,or 21 around 87 etc.........
#also its not that accurate it still would be almost impossible to guess unless u get lucky 

import random

#main game loop
def main():
    while True:
        lives=7 #number of lives
        lower_bound=1 #lower number boundary for guess range
        upper_bound=100 # upper boundary number for the max estimated guess
        guess=random.randrange(1,100)
        option=input(">would you like to exit or ('continue press[ENTER]')")
        if option =="exit":
            print(">bye")
            break
        else:
            print(">WELCOME to the game!")
            print(">simple just gues correct and you win its endless guessing game")
            while lives > 0:
                intake=int(input(f">enter a number around {lower_bound} and {upper_bound} "))
                if intake==guess:
                    print(">correct")
                    break
                elif intake < guess:
                    print(">mid answer close")
                    lower_bound=max(lower_bound,intake+1) #raises  the boundaries of the possible number guess range
                    lives-=1
                    print(f">You have {lives} lives left.")
                else:
                    upper_bound=min(upper_bound,intake-1) #reduces the boundaries of the possible number guess range
                    lives-=1
                    print(f">WRONG left lives:{lives}")
            if lives==0:
                print(">game over")
                  # ask if player wants to play again
            intake_again = input(">Type 'exit' to quit, or press ENTER to play again: ")
            if intake_again.lower() == "exit":
                    print(">Thanks for playing!")
                    break
if __name__=="__main__": #main function to run the game
    main()
