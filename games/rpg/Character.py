class Character:
    name = "Unknown"

    health = 1
    damage = 1
    level = 1

    def __init__(self, name):
        self.name = name

class Ally(Character):
    def __init__(self, name):
        super().__init__(name)

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)