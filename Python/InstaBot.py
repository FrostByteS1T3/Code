import webbrowser
from pynput.mouse import Button, Controller
from time import sleep
import pynput.keyboard
import os
from random import randint
from Words import get_random_word
mouse = Controller()
keyb = pynput.keyboard.Controller()
'''
  ////////////////////
 //Button Locations//
////////////////////
'''
emaill = (825, 400)
name = (825, 440)
uname = (825, 480)
passw = (825, 525)
sign_up = (825, 580)

searchbar = (725, 150)
target = (700, 200)
followb = (800, 260)
user = (1200, 150)
gear = (910, 260)
logout = (720, 640)

url = 'https://www.instagram.com/'

f = open('Accounts.txt', 'a')

hexlist = open('HexList.txt', 'r')


def close_tab():
    keyb.press(pynput.keyboard.Key.cmd_l)
    typ('w')
    keyb.release(pynput.keyboard.Key.cmd_l)


def email():
    suffix = '@gmail.com'
    rand = randint(1000000, 1000000000)
    email = str(rand) + suffix
    f.write(email + '\n')
    return email


def password():
    password = str(randint(10000000, 99999999))
    f.write(password + '\n')
    return password


def make_acc():
    webbrowser.get('chrome').open_new(url)
    sleep(8)
    button(emaill)
    typ(email())
    button(name)
    typ(password())
    button(uname)
    typ(get_random_word(5, 5))
    typ(password())
    button(passw)
    typ(password())
    button(sign_up)
    sleep(3)


def follow():
    button(searchbar)
    typ('sinrew_mtb')
    sleep(3)
    button(target)
    sleep(3)
    button(followb)
    sleep(2)
    button(user)
    sleep(1)
    button(gear)
    sleep(.5)
    button(logout)


def button(loc):
    mouse.position = loc
    sleep(0.1)
    mouse.click(Button.left, 1)
    sleep(0.2)


def typ(text):
    sleep(0.1)
    keyb.type(text)
    sleep(0.1)


ping = 'google.com'

index = [0, 1, 2, 3, 4, 5]
while True:
    sleep(5)
    #os.system('cd ..')
    #os.system('cd ..')
    #os.system('cd ..')
    #os.system('cd SpoofMAC/')
    hmac = hexlist.readline()
    os.system('sudo python3 SpoofMac/scripts/spoof-mac.py randomize en0')
    sleep(5)
    os.system(
        'networksetup -setairportnetwork en0 md6312_5g ThePresharedKeyFor30thAveNW'
    )
    response = os.system("ping -c 1 " + ping)
    #while response != 0:
    #response = os.system("ping -c 1 " + ping)
    #sleep(1)
    os.system(
        'networksetup -setairportnetwork en0 md6312 ThePresharedKeyFor30thAveNW'
    )
    sleep(5)
    make_acc()
    sleep(3)
    #annoy()os.popen('openssl rand -hex 6 | sed \'s/\\(..\\)/\1:/g; s/.$//').read()

    follow()
    close_tab()