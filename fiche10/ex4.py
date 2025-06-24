temp = float(input("Temperature: "))
sign = ""

formula_F = (9 * temp) / 5 + 32
formula_C = (temp - 32) * 5 / 9

while sign != "F" and sign != "C":
    sign = input("Sign (C ou F): ").upper()

    if sign == "F":
        print(round(formula_C, 1), "C")
    elif sign == "C":
        print(round(formula_F, 1), "F")
    else:
        print("Invalid sign")