import pyxel

pyxel.init(64, 64)

def draw():
    ship = pyxel.load("Heart.png")
    pyxel.blt(45, 45, ship, 0, 0, 16, 16, 0)
def update():
    if pyxel.btn(KEY_Q) == True:
        pyxel.quit()
pyxel.run(draw, update)