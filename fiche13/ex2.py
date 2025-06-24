def distincte(str):
    for x in str:
        if str.count(x) > 1:
            return False
    return True

x = input("Name: ")
print(f"Distincte: {distincte(x)}")