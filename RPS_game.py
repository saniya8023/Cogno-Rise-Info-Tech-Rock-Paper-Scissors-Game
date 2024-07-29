import random

def play_game():
    while True: 
        choices = ['rock', 'paper', 'scissors']
        user = str(input('Enter your choice(rock/paper/scissors): ')).strip().lower()
        computer = random.choice(choices)

        while user not in choices:
            print('Please enter a valid choice!')
            user = str(input('Enter your choice(rock/paper/scissors): ')).strip().lower()

        if user == computer:
            print('It is a tie!')
        elif winner(user, computer):
            print('You Won!')
        else:
            print('Computer Won!')

        play_again = str(input('Do you want to play again? (yes/no): ')).strip().lower()
        if play_again != 'yes':
            print('Goodbye')
            break  

def winner(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or \
       (player == 'scissors' and opponent == 'paper') or \
       (player == 'paper' and opponent == 'rock'):
        return True  
    else:
        return False  

play_game()