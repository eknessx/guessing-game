bowl=["apple","banna","cherry","orange","mango"]
modifier=input("choose modifier: remove,add,modify:")
if modifier=="remove":
    remove=input("choose fruit to remove: ")
    bowl.remove(remove)
    print(bowl)
elif modifier=="add":
    add=input("choose fruit to add ")
    bowl.append(add)
    print(bowl)
elif modifier=="modify":
    modify=input("choose fruit to modify: ")
    new_fruit=input("choose new fruit: ")
    index=bowl.index(modify)
    bowl[index]=new_fruit
    print(bowl)
else:
    print("nothing")