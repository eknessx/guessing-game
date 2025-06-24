sw=True
nb=int(input("nombre premier"))
for x in range(2,nb):
    if nb%x==0:
        sw=False
        break
if sw:
    print("premier")
else:
    print("non-premier")
