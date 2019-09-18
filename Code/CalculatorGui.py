from appjar import gui

app = gui()
def press(name):
    if name == 'Exit':
        app.stop()
    else:
        try:
            first_num = int(app.getEntry('first'))
            second_num = int(app.getEntry('second'))

            message = 'The results are:\n\n'
            message += 'Addition: ' + str(first_num + second_num) + '\n'
            message += 'Subtraction: ' + str(first_num - second_num) + '\n'
            message += 'Multiplication: ' + str(first_num * second_num) + '\n'
            message += 'Division: ' + str(first_num / second_num) + '\n'
            if name == 'Result':
                app.setLabel('Result', message)
            elif name == 'MessageBox Result':
                app.infoBox('Result', message)
        except ValueError as e:
            app.errorBox('Error', 'Invalid number')
            app.setFocus('first')
app.addLabel('fn', 'First number', 0, 0)
app.addEntry('first', 0, 1)
app.addLabel('sn', 'Second number', 0 , 2)
app.addEntry('second', 0, 3)
app.setFocus('first')
app.addEmptyLabel('Result', 1, 0, 4)
app.setLabelReleif('Result', app.GROOVE)
app.setLabelAlign('Result', app.NW)
app.setLabelHeight('Result', 8)
app.addButtons(['Result', 'MessageBox Result', 'Exit'], press, 2, 0, 4)
app.go()