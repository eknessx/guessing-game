l = []

x = int(input("List size: "))
for i in range(x):
    l.append(input(f"Value {i}: "))

y = input("Value to search: ")
if l.count(y) > 0:
    print(f"Index: {l.index(y)}")
    l.remove(y)
    print(l)
else:
    print("Value not available")