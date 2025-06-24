#Faire le code python qui trouve les nb parfaits entre 1 et 100
#nb parfait est equale a la somme de ses diviseurs sauf lui meme
#ex 6; 1+2+3 = 6 nb parfait
#ex 10; 1+2+5 = 8 nb non parfait

for x in range(1, 101):
    s = 0
    for y in range(1, x):
        if x % y == 0:
            s += y
    if s == x:
        print(x)