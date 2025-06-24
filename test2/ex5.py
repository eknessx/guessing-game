#list of words upper and lower case
pool = ["OW", "hello", "PARDON", "and", "WAIT"]

#function to call it 
def strin():
        for x in pool:
            if x.isupper:
                print(f"Upper case word: {x}")
            elif x.islower:
                print(f"Upper case word: {x}")
            else:
                print(f"Mixed case word: {x}") # Handle words with mixed casing
strin()
