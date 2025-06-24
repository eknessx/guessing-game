def dif_colors(color1,color2):
    listt=[]
    for x in color1 :
        if x not in color2:
            listt.append(x)
            return set(listt)
    