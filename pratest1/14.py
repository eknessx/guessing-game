def get():
    m=int(input("Count: "))
    return m

def dict_add(m):
    dict_name={}
    dict_age={}
    dict_note={}


    for x in range(m):
        print(f"name {x+1}")
        k=input("enter the key: ")
        z=input("enter the name: ")
        dict_name[k]=z
        y=input("enter l'age: ")
        dict_age[k]=z

        l=[]

        for ipo in range(3):
            l.append(float(input(f"grade {ipo+1}: ")))
        dict_note[k]=l

    return dict_name , dict_age , dict_note


def moy(a):
    s=0
    s+=a[0]*3
    s+=a[1]*5
    s+=a[2]*3
    return s/11

m=get()

dic_name,dict_age,dict_grade=dict_add(m)

for r in dic_name:
    print(f"Name: {dic_name[r]}")
    print(f"age: {dict_age[r]}")
    print(f"notes: {dict_grade[r]}")
    print(f"avrege: {moy(dict_grade[r])}")
    
