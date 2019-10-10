import random
max = int(input('number between 10 and 1000 '))
max_guesses = input('max guesses [1-10] ')
guesses = int(max_guesses)
rand = random.randint(1, max)




def get_guess(max):
    guess = input('Enter a number between 1 and ' + str(max) + ' ')
    return guess
game_played = False
def game(rand, guesses, game_played):
    if guesses > 1:
        game_played = True
        guess = get_guess(max)
        if int(guess) > int(rand):
            print('Too high')
            guesses -= 1
            print('You have ' + str(guesses) + ' guesses left' )
            game(guesses, max, game_played)
        elif int(guess) < rand:
            print('Too low')
            guesses -= 1
            print('You have ' + str(guesses) + ' guesses left' )
            game(guesses, max, game_played)
        elif int(guess) == rand:
            print('You won!')
    else:
        print('Out of guesses')
game(rand, guesses, game_played)