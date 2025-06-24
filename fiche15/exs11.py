#Write a Python program to add all the elements of a dictionary.
s=0
mydict={
    "data1":100,
    "data2":-54,
    "data3":247,
}
for x in mydict.values():
      s+=x
print(s)