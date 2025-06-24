#entrer votre nom, afficher la 1ere et la derniere lettre de votre nom avec la taille du nom
name = input("Name: ")

print(name[0], name[-1])
print(len(name))
print(type(name))
print(name[len(name)//2])
print(name[0:4:2])
