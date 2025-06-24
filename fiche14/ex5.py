s = "Python est un language de programmation"

def flipWords(ch):
    s2 = ch.split()
    s2[0], s2[-1] = s2[-1], s2[0]
    return " ".join(s2)

print(flipWords(s))