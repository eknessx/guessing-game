class Fight:
    allies = []
    enemies = []

    def __init__(self, allies, enemies):
        self.allies = allies
        self.enemies = enemies

    def alliesAlive(self):
        cond = False
        for x in self.allies:
            if x.health > 0:
                cond = True
                break
        return cond
    
    def enemiesAlive(self):
        cond = False
        for x in self.enemies:
            if x.health > 0:
                cond = True
                break
        return cond

    def start(self):

        while self.alliesAlive() and self.enemiesAlive():
            print("a")