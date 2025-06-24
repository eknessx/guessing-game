tu=(5,12,3)
def algo(t):
    m=1
    for x  in t:
        m**=x
    return m
print(algo(tu))