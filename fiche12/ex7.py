tu = (1, 2, 3, 1, 2, 5, 6, 6)

def tupleRepeats(t):
    l = []
    for x in t:
        if t.count(x) > 1:
            if x not in l:
                l.append(x)
    return l

print(tupleRepeats(tu))