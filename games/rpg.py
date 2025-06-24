global health
global enemyHealth
health = 150
enemyHealth = 50

def startGame():
    print("This is an RPG")
    fight()

def chooseAction():
    print("What will you do?")
    print("1-punch")

    return input(">")

def doAction(opt):
    if opt == "1":
        print("Safa2to 3a ni3o")
        globals.__get__("enemyHealth") -= 10

def doEnemyAction(opt):
    if opt == 1:
        print("Safa2ak 3a ni3ak!")
        globals.__get__("health") -= 20

def fight():
    globals.__get__("health") = 150
    globals.__get__("enemyHealth") = 50
    
    while globals.__get__("health") > 0 and globals.__get__("enemyHealth") > 0:
        print("Your health:", globals.__get__("health"), "Enemy health:", globals.__get__("enemyHealth"))

        x = chooseAction()
        doAction(x)
        doEnemyAction(1)

startGame()