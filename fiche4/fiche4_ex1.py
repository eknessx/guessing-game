#ecrire le code python pour valider le jour et le mois entres de facon que le jour soit entre 1 et 31 et le mois soit entre 1 et 12
d = int(input("Day: "))

while d < 1 or d > 31:
    d = int(input("Incorrect day, try again: "))
print("Correct day.")

m = int(input("Month: "))

while m < 1 or m > 12:
    m = int(input("Incorrect month, try again: "))
print("Correct month.")

print("Correct date.")
