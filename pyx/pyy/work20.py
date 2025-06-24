import math

def calculator():
    print("choose operation:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exponentiation")
    print("6. square root")
    print("7. logarithm")
    print("8. sine")
    print("9. cosine")


    input_num = int(input("Enter operation number: "))
    
    if input_num == 1: 
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = num1 + num2
        print(f"result: {result}")
    elif input_num == 2: 
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = num1 - num2
        print(f"result: {result}")
    elif input_num == 3:  
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        result = num1 * num2
        print(f"result: {result}")
    elif input_num == 4:  
        num1 = float(input("enter a number: "))
        num2 = float(input("enter a number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"result: {result}")
    elif input_num == 5: 
        num1 = float(input("enter base: "))
        num2 = float(input("enter exponent: "))
        result = math.pow(num1, num2)
        print(f"result: {result}")
    elif input_num == 6: 
        num1 = float(input("enter a number: "))
        if num1 < 0:
            print("Error: Cannot calculate square root of a negative number.")
        else:
            result = math.sqrt(num1)
            print(f"result: {result}")
    elif input_num == 7:  
        num1 = float(input("enter a number: "))
        num2 = float(input("enter base (default is e): "))
        if num1 <= 0:
            print("Error: Logarithm is not defined for non-positive numbers.")
        else:
            if num2 <= 0:
                print("Error: Logarithm base must be positive and not 1.")
            elif num2 == 1:
                print("Error: Logarithm base cannot be 1.")
            else:
                result = math.log(num1, num2) 
                print(f"result: {result}")
    elif input_num == 8:  
        num1 = float(input("enter angle in radians: "))
        result = math.sin(num1)
        print(f"result: {result}")
    elif input_num == 9: 
        num1 = float(input("enter angle in radians: "))
        result = math.cos(num1) 
        print(f"result: {result}")
    else:
        print("Invalid operation number. Try again")

calculator()