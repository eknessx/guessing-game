numbers=[1,2,3,4,5]
while numbers in range(6):
    numbers+=1
    if numbers==5:
        print(numbers)
        continue
    print(numbers)
    break
