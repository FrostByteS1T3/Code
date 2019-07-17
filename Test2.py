def test(prompt, retries=1, complaint='Name please'):
    while True:
        Name = raw_input(prompt)
        if Name == 'saul':
            return True
test('Wat ur name?')
