import random

game_played = False
def get_number(max_number):
    num = random.randint(0, max_number)
    return num
def get_guesses(max_guesses):
    if game_played == False:
        guesses = max_guesses
    if game_played == True:
        guesses -= 1
    return guesses
def get_max_guesses():
    max_guesses = input('Max guesses [2-20] ')
    if max_guesses > 20 or max_guesses < 2:
        raise ValueError('Not between 2 and 20')
    else:
        return max_guesses

number = int
max_number = 11
def get_max_number():
    max_number = input('Max number [10 - 1000] ')
    if max_number < 10 or max_number > 1000:
        raise ValueError('Not between 10 and 1000')
    else:
        return max_number
def play():
    number = get_number(get_max_number())
play()
print(number)