import final2
tmp=float(input("enter tmp: "))
unite=input("Tc or Tf ")
while unite !="Tf" and unite!="Tc":
    unite=input("Tf or Tc: ")
if unite=="Tf":
    tmp=(tmp-32)*5/9
else:
    tmp=((9*tmp)/5)+32
print(f"the temp is:{(round(tmp, 1))}")