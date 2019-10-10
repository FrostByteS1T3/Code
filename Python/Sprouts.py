import pyxel, os

WIDTH = 100
HEIGHT = 120
BACKGROUND_COLOR = 7
XONE = 45
XTWO = 55
YONE = 60
DOT_COLOR = 0
LINE_COLOR = 6

class Dot:
    def __init__(self):
        
        self.size = 1
        self.connections = 0
    
    def draw(self, x, y):
        pyxel.pix(x, y, DOT_COLOR)


class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        pyxel.run(self.update, self.draw)

    def setup(self):
        Dot.draw(self, XONE, YONE)
        Dot.draw(self, XTWO, YONE)
    def draw(self):
        pyxel.cls(col=BACKGROUND_COLOR)
        self.setup()
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

Game()
