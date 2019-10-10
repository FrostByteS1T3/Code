import webbrowser
from pynput.mouse import Button, Controller
from time import sleep
import pynput.keyboard
from random import randint
mouse = Controller()
keyb = pynput.keyboard.Controller()
BUTTON1 = (620, 310)
BUTTON2 = (600, 420)
URL = 'https://www.textnow.com/signup'

f = open('Accounts.txt', 'a')


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


def make():
    webbrowser.open_new(URL)
    sleep(3)
    mouse.position = BUTTON1
    mouse.click(Button.left, 1)
    keyb.type(email())
    sleep(.2)
    mouse.position = BUTTON2
    mouse.click(Button.left, 1)
    keyb.type(password())


if __name__ == "__main__":
    make()