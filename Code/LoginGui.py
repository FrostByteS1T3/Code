from appjar import gui

app = gui()
app.setBg('green')
app.setTitle('Login')
app.setFg('white')
app.addLabel('Top', 'Login Form')
app.setFont('16')
app.addLabelEntry('Username')
app.addSecretLabelEntry('Password')
def press(b1):
    print(b1, 'pressed')
    if b1 == 'Cancel':
        app.stop()
    elif b1 == 'Reset':
        app.clearEntry('Username')
        app.clearEntry('Password')
        app.setFocus('Username')
    elif b1 == 'Submit':
        username = app.getEntry('Username')
        password = app.getEntry('Password')
    if username == 'saul' and password == 'password':
        app.infoBox('Success', 'Access granted')
    else:
        app.errorBox('Incorrect password', 'Access Denied')
app.addButtons( ['Submit', 'Reset', 'Cancel'], press)
app.go()