#Write a Python program to map two lists into a dictionary.
key=["name","nickname","age"]
value=["alice","hunter",21]

d=dict()
for x in range(len(key)):
    d[key[x]]=value[x]
print(d)