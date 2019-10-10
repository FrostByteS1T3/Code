from pynput.keyboard import Key, Controller

import time

k = Controller()

def press(key):
    k.press(str(key))
    k.release(str(key))

