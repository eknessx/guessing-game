import os

import Character
from Fight import Fight

def clear():
    os.system('cls')

def drawGUI():
    print("Enemies: ")

Fight([Character.Ally("ally")], [Character.Enemy("enemy")]).start()