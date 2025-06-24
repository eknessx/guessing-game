#dictianry with keys to refine to the function what type conversion it needs
data={
    "type1":"str",
    "type2":"dict",
    "type3":"list",
    "type4":"int",
    "type5":"float",
    "type6":"tuple",
    "type7":"set",
}


def main():
    for z in data.values():
        print(z)
    x = input("choose type convert: ")
    if x == "str":
        x2 = input("enter the value: ")
        x2_str = str(x2)
        print(f"converted to {x2_str}")

    elif x == "dict":
        di1 = input("enter the key: ")
        di2 = input("enter the value: ")
        new_dict = {di1: di2}  # Create a dictionary
        print(f"A new dict created: {new_dict}")

    elif x == "int":
        x2 = input("enter the value: ")
        if x2.isnumeric():
            x2_int = int(x2)
            print(f"now the string number is a number {x2_int}")

    elif x == "float":
        x2 = input("enter the value: ")
        x2_float = float(x2)
        print(f"now the string number is a decimal number {x2_float}")

    elif x == "tuple":
        sku = input("enter a string or any value: ")
        new_tuple = (sku,)
        print(f"new tuple been created: {new_tuple}")

    elif x == "set":
        set_elements = input("Enter elements for the set (separated by spaces): ").split()
        new_set = set(set_elements)
        print(f"A new set has been created: {new_set}")

if __name__=="__main__":
    main() #run the code 
