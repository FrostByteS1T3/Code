import hashlib
import base64
from appjar import gui
import os
import time
from GenerateMaster import generate_master
import VerifyMaster
import AESEncryption

def go(password):

    print('Good to go!')

    win = gui()


    def deleteLine(name):
        fn = 'Passwords.txt'
        f = open(fn)
        output = []
        str=name
        for line in f:
            if not line.startswith(str):
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

    def buttons(b1):
        print(b1)
        if b1 == 'Exit':
            win.stop()
        if b1 == 'Create':
            f = open('Passwords.txt', 'a')
            content = win.getEntry('Password')
            encrypted_pass = AESEncryption.encrypt2(content)
            # writes data to file
            f.write(win.getEntry('Name') + '\t' + win.getEntry('Username') + '\t')
            f.close()
            f = open('Passwords.txt', 'ab')
            f.write(encrypted_pass + '\n')
            f.close()
            #win.clearAllEntries()
        if b1 == 'Delete':
            name_to_delete = win.getEntry('Name')
            deleteLine(name_to_delete)
            #win.clearAllEntries()
        if b1 == 'Read':
            AESEncryption.decrypt2(win.getEntry('Name'))
            
    def start_gui():
        #time.sleep(10)

        
        win.setBg('Light blue')
        win.setFg('Black')
        win.addLabel('PyWallet')
        win.addLabelEntry('Name', 2)
        win.addLabelEntry('Username', 3)
        win.addLabelEntry('Password', 4)
        win.addLabel('', 'Password Wallet', 1, 0, 0)
        win.addLabel('blankspace1', '', 5, 0, 0)
        win.addButtons(['Create', 'Delete', 'Edit', 'Read', 'Exit'], buttons, 6, 0, 0)


        win.go()


    start_gui()
app = gui()

def press():
    password = app.getEntry('Password')
    result = VerifyMaster.verify_master(password)
    if result == True:
        app.stop()
        go(password)
    else:
        time.sleep(2)
        app.setLabel('Result', 'Incorrect password')
app.addLabel('Login')
app.setBg('Light blue')
app.addLabel('Result', '')
app.addSecretLabelEntry('Password')
app.addButton('Submit', press)
app.go()


