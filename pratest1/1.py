l1 = ["Charbel", "Angelo", "Majd", "Jason", "Elia", "Celine"]
l2 = ["brown", "red", "yellow", "green"]
l3 = [10, 4, 3 ,9, 1, 5]

l4 = l1 + l2
print(l4)

l2.reverse()
print(l2)

x = int(input(f"Index from 0 to {len(l1) - 1}: "))
l1.pop(x)
print(l1)

l2.remove("red")
print(l2)

l3.append(12)
l3.sort()
print(l3)

x = sum(l3)
print(f"Sum: {x}")
x = x/len(l3)
print(f"Average: {x}")
print(f"Min: {min(l3)}")
print(f"Max: {max(l3)}")

l5 = []
for i in l1:
    l5.append(int(input(f"Age of {i}: ")))
print(l5)