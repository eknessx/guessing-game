enter=list(input("enter name "))
voyelles=['o','a','e','i','o','y','u','A','E','I','O','Y','U']
for x in range(0,len(enter)):
    if enter[x] in voyelles:
        print(enter[x])
    else:
        enter[x]='*'
print(enter)
enter=''.join(enter)
print(enter)
