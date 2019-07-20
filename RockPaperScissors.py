import random
computer = ''
choices = ['rock', 'paper', 'scissors']
def computer_choice():
    computer = choices[random.randint(0,2)]
    return computer
def player_choice():
    player = input('Rock [r], paper [p], or scissors [s]? ')
    if player == 'r':
        return choices[0]
    elif player == 'p':
        return choices[1]
    elif player == 's':
        return choices[2]
    else:
        raise ValueError('Not an option')
play_again = ''
game_played = False
def game():
    c = computer_choice()
    p = player_choice()
    if c == 'rock' and p == 'rock':
        print('The computer chose rock')
        print('It\'s a tie')
    elif c == 'rock' and p == 'paper':
        print('The computer chose rock')
        print('You win!')
    elif c == 'rock' and p == 'scissors':
        print('The computer chose rock')
        print('You lose')
    elif c == 'paper' and p == 'rock':
        print('The computer chose paper')
        print('You lose')
    elif c == 'paper' and p == 'paper':
        print('The computer chose paper')
        print('It\'s a tie')
    elif c == 'paper' and p == 'scissors':
        print('The computer chose paper')
        print('You win!')
    elif c == 'scissors' and p == 'rock':
        print('The computer chose scissors')
        print('You win!')
    elif c == 'scissors' and p == 'paper':
        print('The computer chose scissors')
        print('You lose')
    elif c == 'scissors' and p == 'scissors':
        print('The computer chose scissors')
        print('It\'s a tie')
    game_played = True
if game_played == False or play_again == 'y':
    game()
    play_again = input('Play again [y] ').lower()
    while play_again == 'y':
        game()
        play_again = input('Play again [y] ').lower()