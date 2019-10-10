from pynput.mouse import Button, Controller
from playsound import playsound
import time
mouse = Controller()

time.sleep(5)

button_coords = (564, 525)
button_x = 564
button_y = 525
playsound('beep-01a.mp3')
mouse.position = (button_coords)
i = 0
time.sleep(0.1)
while mouse.position == button_coords:
    mouse.press(Button.left)