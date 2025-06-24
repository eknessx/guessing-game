n = input("Word: ")
n = list(n)
v = "aeiouyAEIOUY "

for x in range(0, len(n)):
    if n[x] in v:
        print(n[x])
    else:
        n[x] = "*"
n = ''.join(n)
print(n)