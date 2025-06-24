thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

x = input("Un fruit: ")
if x in thislist:
    print(f"Yes, {x} is in the fruits list")
else:
    print(f"No, {x} is not in the fruits list")