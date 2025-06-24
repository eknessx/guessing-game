#Ecrire le code python qui accept une sequence du nombre separer par des virgules de l'user et genere une liste puis un tuple de cette sequence
numbersList = input("Numbers seperated by ',': ").split(',')
numbersTuple = tuple(numbersList)
print(numbersList)
print(numbersTuple)