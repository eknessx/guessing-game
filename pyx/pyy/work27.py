class Noob:
    def __init__(self,lvl,status):
        self.lvl=lvl
        self.status=status

class Nob(Noob):
    def __init__(self, lvl, status):
        super().__init__(lvl, status)
        if self.lvl>10:
            print("strong")
        else:
            print("weak")
    
user=Nob(status="yes",lvl=1)
print(user)




    