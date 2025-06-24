#Ecrivez un programme Python pour vérifier si une clé donnée existe déjà dans un dictionnaire.
value={
    "user":"majd",
    "status":"avaible",
    "id":"student",
}

def getid():
    ip=input("enter a key ")
    if ip in value:
        print(f"the key exist")
    else: 
        print("dosen't exist")
getid()
        