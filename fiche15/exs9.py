#Write a Python script to generate and print a dictionary containing a number (between 1 and n) in the form (x, x * x).
bt1={}
n=int(input("enter a number "))

def generate(n):
    for x in range(1,n+1):
        bt1[x] = x*x
    print(bt1)
generate(n)