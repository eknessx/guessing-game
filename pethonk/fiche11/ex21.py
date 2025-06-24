def coeff(n1,n2,coef):
    note=moy(n1,n2)*coef
    return note
def moy(n1,n2):
    m=(n1+n2)/2
    return m 
note1=float(input("enter one: "))
note2=float(input("enter two: "))
print(coeff(note1,note2,18))