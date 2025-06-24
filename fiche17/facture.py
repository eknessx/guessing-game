#main fucntion for the exercice
def factor(n):
    factors = []
    sqrt_n = int(n ** 0.5) + 1
    for x in range(1, sqrt_n):
        if n % x == 0:
            factors.append(x)
            if x != n // x:
                factors.append(n // x)
    return sorted(factors)

#error handling
try:
    number = int(input("Enter the number to factor: "))
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        result = factor(number)
        print(f"Factors of {number}: {result}")
except ValueError:
    print("Error: enter a valid integer.")