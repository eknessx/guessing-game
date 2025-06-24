name_enter=(input("enter name:"))
vowwels=["a","e","o","i","u","l","A","E","O","I","U","L"]
for x in range(0,len(name_enter)):
 if name_enter[x] in vowwels:

        print(name_enter[x])
 else:
        name_enter[x]='*'
print(name_enter)
enter=''.join(name_enter)
print(name_enter)



