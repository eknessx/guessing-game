def coefficient(n1, n2, coef):
    note = moyenne(n1, n2) * coef
    return note

def moyenne(n1, n2):
    m = n1 + n2
    return m / 2

note1 = float(input("note 1: "))
note2 = float(input("note 2: "))

print(coefficient(note1, note2, 18))