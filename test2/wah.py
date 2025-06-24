import math

#dictionary to index the diffrent operations
operations = {
    "modulos": "%",
    "division": "/",
    "addition": "+",
    "subtraction": "-",
    "cos": "cos",  # Special case
    "sin": "sin",   # Special case
    "exit": "exit"
}

#loop for the proggramm
while True:
    print("available operations")
    for key in operations:
        print(key)

    enter1 = input("Enter the operation (or 'exit'): ").lower()
    if enter1 == "exit":
        print("bye")
        break

    if enter1 not in operations:
        print("Invalid operation.")
        continue

    operation = operations.get(enter1)

    try:
        if operation in ("cos", "sin"):
            enterx = float(input("Enter the number: "))
        else:
            enterx = float(input("Enter the first number: "))
            enterz = float(input("Enter the second number: "))

        if operation == "%":
            result = enterx % enterz
        elif operation == "/":
            if enterz == 0:
                print("Cannot divide by zero")
                continue
            result = enterx / enterz
        elif operation == "+":
            result = enterx + enterz
        elif operation == "-":
            result = enterx - enterz
        elif operation == "cos":
            result = math.cos(enterx)
        elif operation == "sin":
            result = math.sin(enterx)

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print("An error occurred:", e)

                    

