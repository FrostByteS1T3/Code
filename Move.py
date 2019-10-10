from pynput.mouse import Button, Controller
import time

m = Controller()
time.sleep(3)
m.position = (760, 370)
m.click(Button.left, 1)