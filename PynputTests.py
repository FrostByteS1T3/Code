from pynput.mouse import Button, Controller
from playsound import playsound
import time
mouse = Controller()

time.sleep(5)

print(mouse.position)

playsound('beep-01a.mp3')