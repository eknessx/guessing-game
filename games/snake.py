import tkinter
from tkinter import Tk, Canvas, Frame, BOTH
import random

class GameWindow(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Snake")
        self.pack(fill=BOTH, expand=0)

class Drawable():
    position = [0, 0]
    size = [25, 25]
    colors = ["#000", "#000"]
    def __init__(self, size, color, position):
        self.position = position
        self.colors = color
        self.size = size
        self.rect = canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1], outline=self.colors[1], fill=self.colors[0])
    
    def update(self):
        canvas.coords(self.rect, self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1])
        canvas.itemconfig(self.rect, outline=self.colors[1], fill=self.colors[0])

class Player:
    delay = 0
    direction = 0

    ydir = False
    xdir = False

    position = [0, 0]
    lastPos = [0, 0]

    snakeParts = []

    #config
    speed = 4
    doWarp = True

    def __init__(self, pos):
        self.position = pos
        self.snakeParts.append(Drawable([32, 32], ["#fff", "#fff"], pos.copy()))

    def update(self):
        self.delay += self.speed
        if self.delay >= 30:
            if self.direction == 0:
                self.position[0] -= 32
            elif self.direction == 1:
                self.position[0] += 32
            elif self.direction == 2:
                self.position[1] -= 32
            elif self.direction == 3:
                self.position[1] += 32
            
            self.xdir = False
            self.ydir = False

        if len(self.snakeParts) < 2:
            if keys.__contains__("a"):
                self.direction = 0
            if keys.__contains__("d"):
                self.direction = 1
            if keys.__contains__("w"):
                self.direction = 2
            if keys.__contains__("s"):
                self.direction = 3
        else:
            if keys.__contains__("a") and not self.direction == 1 and not self.ydir:
                self.direction = 0
                self.xdir = True
            if keys.__contains__("d") and not self.direction == 0 and not self.ydir:
                self.direction = 1
                self.xdir = True
            if keys.__contains__("w") and not self.direction == 3 and not self.xdir:
                self.direction = 2
                self.ydir = True
            if keys.__contains__("s") and not self.direction == 2 and not self.xdir:
                self.direction = 3
                self.ydir = True

        if self.doWarp:
            if self.position[0] < 0:
                self.position[0] = 320 - 32
            if self.position[0] >= 320:
                self.position[0] = 0
            if self.position[1] < 0:
                self.position[1] = 320 - 32
            if self.position[1] >= 320:
                self.position[1] = 0
        else:
            if self.position[0] < 0 or self.position[0] >= 320 or self.position[1] < 0 or self.position[1] >= 320:
                exit()

        if self.delay >= 30:
            self.delay -= 30
            s = self.snakeParts[len(self.snakeParts) - 1]
            self.lastPos = s.position.copy()
            s.position = self.position.copy()
            self.snakeParts.remove(s)
            self.snakeParts.insert(0, s)

        for x in self.snakeParts:
            x.update()

class Game():
    player = None

    apples = []
    score = 0

    scoreText = None

    def __init__(self):
        Drawable([640,640], ["#000","#000"], [0,0])
        self.player = Player([64, 64])
        self.randomApple()
        self.scoreText = canvas.create_text((160, 320 + 16), text="Score: 0", fill="#fff", font=("Segoe UI", 16))

    def update(self):
        self.player.update()

        canvas.itemconfig(self.scoreText, text=f"Score: {self.score}")

        for x in self.apples:
            if x.position[0] == self.player.position[0] and x.position[1] == self.player.position[1]:
                canvas.delete(x.rect)
                self.apples.remove(x)
                self.score += 1
                self.randomApple()
                self.player.snakeParts.append(Drawable([32, 32], ["#fff", "#fff"], self.player.lastPos.copy()))
        
        for x in self.player.snakeParts:
            if x != self.player.snakeParts[0] and x.position[0] == self.player.position[0] and x.position[1] == self.player.position[1]:
                exit()

    def randomApple(self):
        x = random.randrange(0, 10) * 32
        y = random.randrange(0, 10) * 32
        apple = Drawable([32,32], ["#f00","#f00"], [x,y])
        self.apples.append(apple)
        for s in self.player.snakeParts:
            if s.position[0] == x and s.position[1] == y:
                self.apples.remove(apple)
                canvas.delete(apple.rect)
                self.randomApple()

    def clear(self):
        for o in self.canvasObjs:
            canvas.delete(o)
        self.canvasObjs = []
        for d in self.drawables:
            canvas.delete(d.rect)
        self.drawables = []

    def keyPress(self, keyIn):
        if not keys.__contains__(keyIn.char):
            keys.append(keyIn.char)

    def keyRelease(self, keyIn):
        if keys.__contains__(keyIn.char):
            keys.remove(keyIn.char)

def gameLoop():
    game.update()

    mainWindow.after(17, gameLoop)

mainWindow = Tk()
win = GameWindow()
mainWindow.geometry("320x352")
canvas = Canvas(mainWindow, highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)
game = Game()
keys = []
mainWindow.bind("<KeyPress>", game.keyPress)
mainWindow.bind("<KeyRelease>", game.keyRelease)
mainWindow.after(17, gameLoop)
mainWindow.resizable(False, False)
mainWindow.mainloop()