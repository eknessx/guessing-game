def FindInParagraph(p, l):
    p2 = p.split(" ")
    for x in p2:
        if x[0] == l:
            print(x)

x = input("Paragraph: ")
l = FindInParagraph(x, "a")