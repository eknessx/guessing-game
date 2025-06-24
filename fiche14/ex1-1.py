#Trouver d'apres une fonction python si le nb est palindrome

def rev(num):
    n = num #1245
    inverse = 0
    while n != 0:
        inverse = (inverse * 10) + (n % 10)
        n //= 10
    return inverse

def Palindrome(num):
    inverse = rev(num)

    if num == inverse:
        return True
    return False

x = int(input("Num: "))
print(Palindrome(x))