numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 824]

def pairsInList(l):
    for x in l:
        if x == 237:
            break
        if x % 2 == 0:
            print(x)

pairsInList(numbers)