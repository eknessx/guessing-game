listr=[1,2,3,4]

def string(l):
    ch=""
    for i in l:
        ch += str(i)
    return ch
print(string(listr))