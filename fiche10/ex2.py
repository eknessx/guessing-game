import datetime

#y = int(input("Year: "))
#m = int(input("Month: "))
#da = int(input("Day: "))

d = datetime.datetime.now()
#dn = datetime.datetime(y, m, da)
dn = datetime.datetime(2008, 7, 12)
print(d - dn)

dn = input("Donner une date separer par /: ")
ln = dn.split("/")
print(ln)
an = ln[0]
mn = ln[1]
jn = ln[2]