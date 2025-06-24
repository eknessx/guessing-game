#Write a Python program to iterate through dictionaries using for loops.

dict1={
    "hanna":"dead",
    "robert":"alive",
    "leo":"who?",
}

def loop():
    for x in dict1:
        print(dict1[x])
loop()