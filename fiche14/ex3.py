#Faire le code python pour enlever un des elements duplicer dans une liste
dup_list = ["Hello", "how", "are", "hello", "you", "are", "my", "how"]

l = []
for x in dup_list:
    if not x in l:
        l.append(x)

print(l)