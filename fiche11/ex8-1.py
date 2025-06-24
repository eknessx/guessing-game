color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

def notInL2(l1, l2):
    return set(l1).difference(l2)

print(notInL2(color_list_1, color_list_2))