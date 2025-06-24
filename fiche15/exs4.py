import math, sys

# THE MAIN FUNCTION
def main():
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('calculated one at a time.')
    print()
    while True:
        print("Enter a number to start searcging for primes from:")
        print("(Try 0 or 1000000000000 (12 zeros) or another number.)")
        option=input(">")
        if option.isdecimal():
            num=int(option)
            break

    input("Press Ctrl-C at any time to quit. Press Enter to begin...")
    while True:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num+1
def  isPrime(number):
    if number < 2:
        return False
    elif number ==2:
        return True
    
    try:
        for x in range(2,int(math.sqrt(number))+1):
            if number % x==0:
                return False
            return True
    except:
        print("error run the program again")
        print("")
        
# main function error handeling
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()