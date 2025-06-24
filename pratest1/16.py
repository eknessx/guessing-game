c2=2
x=1
while x==1:
    d=input("enter a number ")
    try:
        d=int(d)
        break
    except ValueError:
        print("must enter a whole number")
        x=1
        continue
    finally:
        print("enter a number ")
f=c2*d
print(f)
