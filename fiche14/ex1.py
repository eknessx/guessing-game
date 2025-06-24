#Trouver d'apres une fonction python si le nb est palindrome

def Palindrome(num):
    x = 1
    y = 0
    l = []
    while num // x > 0:
        x *= 10
        y += 1

    r = num
    x = x // 10
    while x >= 1:
        l.append(r // x)
        r = r % x
        x = x // 10

    l.reverse()

    if num == int(str(num)[::-1]):
        return True
    return False

x = int(input("Num: "))
print(Palindrome(x))