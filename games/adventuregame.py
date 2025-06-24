global inventory
inventory = []

def getIn():
    x = input()
    if x == "inv":
        inv()
    return x

def inv():
    if len(getVar("inventory")) == 0:
        print("Your inventory is empty!")
        x = getIn()
        return
    print("You check your inventory, it contains:")
    for item in range(0, len(getVar("inventory")), 2):
        if getVar("inventory")[item + 1][1] != 1:
            print(f">{getVar("inventory")[item + 1][1]} {getVar("inventory")[item + 1][0]}")
        else:
            print(f">{getVar("inventory")[item + 1][1]} {getVar("inventory")[item]}")
    x = getIn()

def getVar(name):
    return globals().get(name)

def mountain():
    print("You are standing on a mountain, you see a house and a base up ahead.")
    print("1-Check the house")
    print("2-Approach the base")
    x = getIn()
    if x == "1":
        house()
    elif x == "2":
        baseGate()
    else:
        mountain()

def house():
    if getVar("inventory").count("ladder"):
        print("The house now doesn't have any items that catch your interest.")
    else:
        print("You step into the house, you find something that resembles a ladder in front of you.")
    print("1-Leave")
    if not getVar("inventory").count("ladder"):
        print("2-Take it")
    x = getIn()
    if x == "1":
        mountain()
    elif x == "2" and not getVar("inventory").count("ladder"):
        print("You decided to take the ladder with you.")
        getVar("inventory").extend(["ladder", ["ladders", 1]])
        house()
    else:
        house()

def baseGate():
    print("You find a tall wall protecting a base, you cannot get through the gate.")
    print("1-Turn back")
    print("none")
    if getVar("inventory").count("ladder"):
        print("2-Use ladder")
    x = getIn()
    if x == "1":
        mountain()
    elif x == "2" and getVar("inventory").count("ladder"):
        print("You used the ladder to climb over the wall.")
        i = getVar("inventory").index("ladder")
        getVar("inventory").pop(i)
        getVar("inventory").pop(i)
        base()
    else:
        baseGate()

def base():
    print("You are inside a strange base, there is 3 buildings:")
    print("1-Enter the big building")
    print("2-Enter the small room")
    print("3-Enter the far room")
    x = getIn()
    if x == "1":
        bigBuilding()
    elif x == "2":
        smallRoom()
    elif x == "3":
        farRoom()
    else:
        base()

def bigBuilding():
    print("a")

def smallRoom():
    print("You enter the small room, you find a")

def farRoom():
    print("a")

def gameover():
    print("Game over.")
    exit()

mountain()