temp = float(input("Temperature: "))
sign = ""

formula_F = (9 * temp) / 5 + 32
formula_C = (temp - 32) * 5 / 9

while sign.capitalize() != "F" and sign.capitalize() != "C":
    sign = input("Sign (C ou F): ")

    if sign.capitalize() == "F":
        print(round(formula_C, 1), "C")
    elif sign.capitalize() == "C":
        print(round(formula_F, 1), "F")
    else:
        print("Invalid sign")