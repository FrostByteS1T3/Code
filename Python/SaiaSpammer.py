import webbrowser
from pynput.mouse import Button, Controller
from time import sleep
import pynput.keyboard
from random import randint
mouse = Controller()
keyb = pynput.keyboard.Controller()
BUTTON1 = (1350, 135)
BUTTON2 = (650, 460)
BUTTON3 = (600, 550)
BUTTON4 = (650, 640)
BUTTON5 = (650, 715)
# saias link URL = 'https://offerup.com/item/detail/760737784/'
URL = 'https://offerup.com/p/65033804/'

f = open('Accounts.txt', 'a')

BUTTON6 = (875, 290)
BUTTON7 = (1190, 210)
BUTTON8 = (1040, 610)  # make offer
BUTTON9 = (650, 615)  # accept ammount
OUT2 = (30, 130)
BUTTON10 = (1000, 350)
BUTTON11 = (1200, 420)
OUT = (875, 630)

BUTT = (455, 843)


def email():
    suffix = '@gmail.com'
    rand = randint(10000, 1000000)
    email = str(rand) + suffix
    f.write(email + '\n')
    return email


def password():
    password = str(randint(10000000, 99999999))
    f.write(password + '\n')
    return password


def make_acc():
    webbrowser.open_new(URL)
    sleep(5)
    button(BUTTON1)
    sleep(0.2)
    button(BUTTON2)
    sleep(0.01)
    typ(email())
    sleep(0.01)
    button(BUTTON3)
    sleep(0.01)
    typ(password())
    sleep(0.01)
    button(BUTTON4)
    sleep(0.01)
    typ(password())
    sleep(0.01)
    button(OUT)
    sleep(0.1)
    button(BUTTON5)
    sleep(0.2)


def follow():
    button(BUTTON6)
    sleep(0.2)
    button(BUTTON7)
    sleep(3)
    button(BUTT)
    sleep(0.2)
    button(BUTTON1)
    sleep(0.5)
    button(BUTTON11)
    sleep(0.2)


def button(loc):
    mouse.position = loc
    sleep(0.1)
    mouse.click(Button.left, 1)


def typ(text):
    keyb.type(text)


def annoy():
    button(BUTTON6)
    sleep(0.2)
    button(BUTTON7)
    sleep(0.2)
    button(BUTTON8)
    sleep(0.2)
    button(BUTTON9)
    sleep(0.2)
    button(BUTTON10)
    sleep(0.3)
    button(OUT2)
    sleep(0.2)
    button(BUTTON1)
    sleep(0.5)
    button(BUTTON11)
    sleep(0.2)


index = [0, 1, 2, 3, 4, 5]
for i in index:
    sleep(8)
    make_acc()
    sleep(3)
    #annoy()
    follow()