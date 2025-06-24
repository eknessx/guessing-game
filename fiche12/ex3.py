#Ecrivez un programme python pour ajouter un element dans un tuple

def tuple_append(t, x):
    t = t + tuple([x])
    return t

tu = (1, 2, 3)
tu = tuple_append(tu, 4)
print(tu)