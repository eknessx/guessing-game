def char(xh):
    for x in xh:
        if xh.count(x)>1:
            return False
    return True
nom=input('chaine ')
print(char(nom))    