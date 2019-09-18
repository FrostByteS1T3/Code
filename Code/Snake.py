import pyxel
from random import randint
from collections import deque, namedtuple

Point = namedtuple("Point", ["x", "y"]) 

COL_BACKGROUND = 3
COL_BODY = 11
COL_HEAD = 7
COL_DEATH = 8
COL_APPLE = 8

TEXT_DEATH = ["GAME OVER", "(Q)UIT", "(R)ESTART"]
COL_TEXT_DEATH = 0
HEIGHT_DEATH = 5

WIDTH = 40
HEIGHT = 50

HEIGHT_SCORE = pyxel.FONT_HEIGHT
COL_SCORE = 6
COL_SCORE_BACKGROUND = 5

UP = Point(0, -1)
DOWN = Point(0, 1)
RIGHT = Point(1, 0)
LEFT = Point(-1, 0)

START = Point(5, 5 + HEIGHT_SCORE)

class Snake():
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption='Snake', scale=8, fps=20)
        self.reset()
    
    def reset(self):
        self.direction = RIGHT
        self.snake = deque()
        self.snake.append(START)
        self.death = False
        self.score = 0
    
    def update(self):
        if not self.dead:
            update_direction()
            update_snake()
            check_death()
            check_apple()
    def update_direction(self):
        if pyxel.btn(pyxel.KEY_UP):
            if self.direction != DOWN:
                self.direction = UP
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.direction != UP:
                self.direction = DOWN
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.direction != RIGHT:
                self.direction = LEFT
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.direction != LEFT:
                self.direction = RIGHT
    def update_snake(self):
        old_head = self.snake[0]
        new_head = Point(old_head.x + self.direction.x, old_head.y + self.direction.y)
        self.snake.appendleft(new_head)
        self.popped_point = self.snake.pop()

    def check_apple(self):
        if self.snake[0] == self.apple:
            self.score += 1
            self.snake.append(self.popped_point)
            self.generate_apple()

            pyxel.play(0, 0)
    def generate_apple(self):

        snake_pixels = set(snake)
        while self.apple in snake_pixels:
            
