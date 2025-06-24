num1=0
num2=-10

numbers=[-2,1,5,-6,7,-1,2,4]
for x in range(0,len(numbers)):
    if num1 and num2 in numbers <0:
        num1+=1
        print(numbers[x])
    else:
        numbers[x]='*'
        num2+=1
print(f"value positive={num1}, value negative={num2}")
