#ecrivez un code python pour verifier si duex ensembles donnes n ont pas acun element en commun
def sets(m,z):
    x=True
    for y in m:
        if y in z:
            x=False 
    return x
    
set1={1,2,7,4,2}
set2={0,4,8,3}
print(sets(set1,set2))
print(set1.isdisjoint(set2))
