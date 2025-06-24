import sys

#main function
def main():
    while True:# main loop
        print("enter the number u wish")
        print("calculate (such as 5, 50, 1000, 9999), or QUIT to quit:")
        option=input(">").upper()
        # if user quits yeah he quits even tho i am the user idk
        if option=="QUIT":
            print("Thanks for playing")# did i even make a game?!
            sys.exit()

        if option.isdecimal() and int(option) !=0:
            xtz = int(option)
            break

        print("enter a number greater than 0,or QUIT")
        if xtz ==1:
            print("0")
            print()
            print("the #1 Fibonacci number is 0")
        elif xtz==2:
            print("0,1")
            print()
            print("the #2 Fibonacci number is 1")
        if xtz >= 10000:
                print('WARNING: This will take a while to display on the')
                print('screen. If you want to quit this program before it is')
                print('done, press Ctrl-C.')# man if u mackbook idk cmd+c?
                input('Press Enter to begin...')

    secondTolastNumber=0
    lastNumber=1
    fibNumbersCalculated=2
    print('0, 1, ', end='')

    # a nother while loop that later display other thing about fibonaci!
    while True:
        nextNumber = secondTolastNumber +lastNumber
        fibNumbersCalculated+=1

        print(nextNumber, end='')
        #checks if we've found the xtz number the user needs:
        if fibNumbersCalculated ==xtz:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                   'number is ', nextNumber, sep='')
            break
        print(" , ", end='')

        secondTolastNumber = lastNumber
        lastNumber = nextNumber

if __name__ =="__main__":
    main() # executes the program