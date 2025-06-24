key=["screen","mouse","keyboard"]
value=["pixels","mice","type"]



d=dict()
def reverse(d):  
    for x in range(len(key)):
        d[value[x]]=key[x]
        print(d)
reverse(d)