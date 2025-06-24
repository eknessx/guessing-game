def FindInParagraph(p, l1, l2):
    p2 = p.split(" ")
    for x in p2:
        if x[0] == l1 or x[-1] == l2:
            print(x)

x = input("Paragraph: ")
l = FindInParagraph(x, "a", "e")