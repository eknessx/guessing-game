#Ecrire le program python pour calculer le nb de jours entre 2 dates donnee
import datetime

d1 = input("Date 1 (year/month/day): ").split("/")
d2 = input("Date 2 (year/month/day): ").split("/")

capital = 10000

dc1 = datetime.date(int(d1[0]), int(d1[1]), int(d1[2]))
dc2 = datetime.date(int(d2[0]), int(d2[1]), int(d2[2]))
diff = dc2 - dc1

print(diff.days, "Days")

inter = (dc2 - dc1).days * capital * 0.001
print(inter, "$")