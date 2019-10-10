import random
number = random.randint(1, 1000)
guesses = 10
def get_guess():
    guess = input('What is your guess [1-1000] ')
    return guess
def game(number, guesses):
    while guesses > 1:
        guess = get_guess()
        if int(guess) > number:
            guesses -= 1
            print('Too high')
            print('You have ' + str(guesses) + ' left')
        elif int(guess) < number:
            guesses -= 1
            print('Too low')
            print('You have ' + str(guesses) + ' left')
        elif int(guess) == number:
            print('You win!')
            break

game(number, guesses)