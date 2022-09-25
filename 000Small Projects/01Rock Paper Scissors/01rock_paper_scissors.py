import random
import time


def game(player, computer):
    machine = 0
    human = 0
    if player == computer:
        time.sleep(0.5)
        print('Draw!')
    elif player == 'S' and computer == 'P' or player == 'P' and computer == 'R' or player == 'R' and computer == 'S':
        human += 1
        time.sleep(0.5)
        print('Player win this round!')
    else:
        machine += 1
        time.sleep(0.5)
        print('Computer win this round!')
    one_more_game = next_game()
    return human, machine, one_more_game


def next_game():
    while True:
        time.sleep(0.2)
        question = input('Another game ? Y/N : ').upper()
        if question == 'Y':
            return True
        elif question == 'N':
            return False
        else:
            time.sleep(0.5)
            print('Invalid answer!')
            continue


moves = ['P', 'R', 'S']
print("Hello, to my first  small game!")
print("Rock, Paper, Scissors!")
name_input = input("Please enter your name: ")
print(f'{name_input}, do you wanna play a game?')

player_scores = 0
computer_scores = 0
another_game = True
while another_game is not False:
    answer = input(f'Y or N: ').upper()
    if answer != 'N' and answer != 'Y':
        print('Invalid input. Try again!')
        continue
    elif answer == 'N':
        print(f'Good bye, {name_input}!')
        time.sleep(1)
        print('GAME   OVER')
        another_game = False
        exit()

    elif answer == 'Y':
        print(f'{name_input}, welcome!')

        while True:
            player_move = input('(P)-Paper, (R)-Rock, (S)-Scissors. Enter your choice: ').upper()
            if player_move not in moves:
                print(f'Invalid, input {name_input}. Please choose, one of shown examples!')
                continue
            time.sleep(0.5)
            print(f'Player, choice is: {player_move}')
            computer_move = random.choice(moves)
            time.sleep(0.5)
            print(f'Computer, choice is: {computer_move}')
            result = game(player_move, computer_move)
            player_scores += result[0]
            computer_scores += result[1]
            another_game = result[2]
            if another_game is False:
                break

time.sleep(0.3)
print(f'Player scores: {player_scores}.')
print(f'Computer scores: {computer_scores}.')
time.sleep(0.3)
if player_scores > computer_scores:
    print('Player win THE GAME!')
elif player_scores < computer_scores:
    print('Computer win THE GAME!')
else:
    print('Equal scores, we don`t have Winner!')
time.sleep(0.3)
print(f"Bye, bye, {name_input}!")
print('GAME   OVER')
