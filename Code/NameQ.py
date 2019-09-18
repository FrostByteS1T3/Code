def test(prompt, retries=1, complaint='Name please'):
    while True:
        Name = raw_input(prompt)
        if Name == 'saul' or Name == 'Saul':
            print 'Wow, what a cool name!'
            return True
        if Name != 'Saul':
            print 'What a gross name.'
test('What is your name? ')
