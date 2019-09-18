import hashlib
from appjar import gui
import os
import time

salt = os.urandom(32)
password = 'Password123'
new_key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
)
app = gui()

def go():
    #time.sleep(10)
    app.stop()
    win = gui()
    win.setBg('Black')
    win.setFg('Green')
    win.addLabel('Top secret access granted.')
    win.addLabel('', '', 1, 4, 6)
    win.go()


def press():
    key = app.getEntry('Password')
    key_e = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    key.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    if new_key == key_e:
        app.setLabel('Result', 'Password is correct')
        time.sleep(5)
        go()
    else:
        time.sleep(5)
        app.setLabel('Result', 'Password is incorrect')
app.addLabel('Login')
app.setBg('Light blue')
app.addLabel('Result', '')
app.addSecretLabelEntry('Password')
app.addButton('Submit', press)
app.go()


