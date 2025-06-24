#Ecrire la fonction python pour multiplier les nb d'un tuple donnee
t = (5, 12, 1, 3)

def mul(t):
    m = 1
    for x in t:
        m *= x
    return m

def moy(t):
    s = sum(t)
    return s/len(t)

print(mul(t))
print(moy(t))