liste=["jason","therese","elie","piere","rita","majd"]

def func1(x):
        liste.append("angelo")
        print(liste)

def func2():
        for x in liste:
                print(x.capitalize())

def func3(x):
        for x in liste:
                print(len(x))

def func4():
        liste.sort()
        print(liste)

def func5():
        print(liste.remove("elie"))

def func6():
        print(liste.pop(2))
        print(liste)

liste_num=[20,19,3,4,12,11,1]

def func7():
        print(sum(liste_num))
        print(sum(liste_num)/len
              (liste_num))
        
def func8():
        for m in range(len(liste_num)):
                if liste_num[m]<10:
                        liste_num[m]+=1 
        print(liste_num) 

def func9():
        liste_piss=[]
        for z in liste_num:
                if z%2==0:
                        liste_piss.append(z)

def func10():
        liste_num[0],liste_num[-1]=liste_num[-1],liste_num[0]
