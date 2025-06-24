def myobjective():
    return True
if myobjective() == 0:
    print('i hate python')
elif myobjective() == 1:
    print('i might think of it')
else:
    print('i love python')

def newobjective():
    return False
if myobjective and newobjective == True:
    print('true facts')
else:
    print('false facts')
