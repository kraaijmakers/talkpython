import random

print('---------------------------------')
print('     Guess that number game!')
print('---------------------------------')
print()

random_number = random.randint(0, 100)


player_name = input('Please enter your name: ')
guess = -1
play_again = 'y'
tries = 0

while play_again == 'y':
    while guess != random_number:
        tries += 1
        guess_text = input('Guess a number between 0 and 100: ')
        guess = int(guess_text)

        if guess < random_number:
            print('I am sorry {}, your guess of {} is too low.'.format(player_name, guess))
        elif guess > random_number:
            print('I am sorry {}, your guess of {} is too high.'.format(player_name, guess))
        else:
            print('Congratulations {}, you won the game in {} tries!'.format(player_name, tries))
    tries = 0
    guess = -1
    random_number = random.randint(0, 100)
    play_again = input('Do you want to play again? Press [Y]: ')

print('Thanks for playing {}!'.format(player_name))
