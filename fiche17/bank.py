#dans une banque pur chaque jour on a interet de 1% sur e mntant entre.on vous demande de trouver l'interet a partir du taux et de 2 dates entrees: date debut et date fin 
#ex:1/1/2025 df 16//202 montant:500


def shit():
    from datetime import date
    date1=date(y1,m1,d1)
    date2=date(y2,m2,d2)
    jour=date1-date2
    return jour.days

def calc():
    interet=(shit()*1*m)/1000
    return interet

m=float(input("montant bq "))
y1=int(input("annee debut "))
m1=int(input("mois debut "))
d1=int(input("jour debut "))
y2=int(input("annee debut "))
m2=int(input("mois fin "))
d2=int(input("annee debut "))

print("wifi",round(calc(),2))