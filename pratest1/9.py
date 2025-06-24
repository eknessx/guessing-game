dict1={
    "dup0":"nana",
    "dup1":"nourr",
    "dup2":"alex",
    "dup3":"majd",
    "dup3":"majd",
}


def remover():
    for x in dict1.values():
        if x==dict1:
            dict1.pop()
        print(x)
remover()