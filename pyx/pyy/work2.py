def myobjective(x):
    for m in range(2, x):
        if x % m == 0:
            return False
    return True
         
x=int(input("enter a prime number "))
print(myobjective(x))
print("this is a prime number")  