def est_palindrome(nombre):
    nombre_str = str(nombre)
    return nombre_str == nombre_str[::-1]

nombre = str(input("Entrez un nombre: "))
if est_palindrome(nombre):
    print(f"{nombre} est un palindrome.car {nombre} est un palindrome : {nombre} == {nombre[::-1]}")
else:
    print(f"{nombre} n'est pas palindrome. car {nombre} n'est pas palindrome : {nombre} == {nombre[::-1]}")

