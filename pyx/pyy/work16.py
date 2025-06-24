def remove_spaces(ch):
    return ' '.join(ch.split())
ch="my      name       is          majd"
print(f"cleaned text: {remove_spaces(ch)} , and spaced text: {ch}")





def spacing(xh):
    b= xh.split()
    c= " "
    for x in b:
        c = c+x+" "
    return c
xh=input("enter a phase ")
print(f"fixed spacings :{spacing(xh)}")




