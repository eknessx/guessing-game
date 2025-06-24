wordsList = input("Paragraph to use: ").split(" ")

y = 0
for x in wordsList:
    if len(x) > 2 and x[0] == x[-1]:
        print(x)
        y += 1
print(f"Il-y-a {y} mots")
