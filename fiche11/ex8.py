color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

def notInL2(l1, l2):
    l = []
    for x in l1:
        if not x in l2:
            l.append(x)
    return set(l)

print(notInL2(color_list_1, color_list_2))