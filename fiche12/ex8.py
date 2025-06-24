x = int(input("Number: "))

tu = (1, 2, 3, 4)

def inTuple(t, x):
    if x in t:
        return t.index(x)
    return -1

print(inTuple(tu, x))