def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print 'you are also cool!'
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print 'you are stupid'
        retries = retries - 1
ask_ok('Is saul cool? ')
