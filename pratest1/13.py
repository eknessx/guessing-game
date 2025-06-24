def distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False
    
print(distinct([1,5,9,7]))
print(distinct([2,4,5,5,7,9]))