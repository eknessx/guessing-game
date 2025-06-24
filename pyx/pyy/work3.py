class user:
    def __init__(self,name,age,sport,lvl):
        self.name=name
        self.age=age
        self.sport=sport
        self.lvl=lvl

class Person(user):
    def __init__(self, name, age, sport, lvl):
        super().__init__(name, age, sport, lvl)
    
x=Person(name="majd",age=16,sport="roller",lvl=999)
print(f"name: {x.name},age: {x.age},lvl: {x.lvl},sport: {x.sport}\n")


