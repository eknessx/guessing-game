operation = input("choose operation: +, -, *, /: ")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")