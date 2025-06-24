#l1 = [1, 2, 3, 4]
#l2 = [5, 6, 7, 8]
#creer une liste 3eme qui est formee de 2 autres listes l1 et l2
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = l1 + l2
l3.append(9)
l3.insert(len(l3) // 2, "center")
print(l3)

l4 = [10]
l4.clear()
print(l4)

l5 = l2
l2[0] = 1
print(l5)

l2 = [5, 6, 7, 8]

l5 = l2
l5[0] = 1
print(l2)

l6 = l2.copy()
l2[3] = "18"
print(l6)

l2 = [5, 6, 7, 8]