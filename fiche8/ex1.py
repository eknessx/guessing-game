voyelles = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', ' ']
n = input("Word: ")
n = list(n)

w = ""

for x in range(0, len(n)):
    if voyelles.count(n[x]) == 0:
        n[x] = "*"
    w += n[x]

print(w)
