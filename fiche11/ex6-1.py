#Ecrire la fonction python qui permet de tirer les valeurs qui se trouvent dans la liste1_color et ne se trouvent pas dans la
#liste2_color
liste1_color = ["yellow", "brown", "red", "black", "white", "blue", "green"]
liste2_color = ["brown", "pink", "blue", "black"]

print(set(liste1_color).difference(liste2_color))

def func(l1, l2):
    l3 = []
    for x in l1:
        if not (x in l2):
            l3.append(x)
    return l3

print(func(liste1_color, liste2_color))