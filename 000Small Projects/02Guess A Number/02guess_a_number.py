import random
import time


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


print('Hello!')
time.sleep(0.3)
print('This is "Guess a number" game!')
time.sleep(0.3)
name = input('Please enter your name: ')
time.sleep(0.4)
print(f'Welcome, to the GAME {name}. Enjoy!')
time.sleep(0.7)
print(f'The computer has a secret.')
time.sleep(1)
print(f'This is a whole number between 1 and 100.')
time.sleep(1.2)
print(f'{name}, try to guess, what is the number!')

game = True
while game is not False:
    computer_number = random.randint(1, 100)

    while True:
        time.sleep(0.4)
        player_number = input('Enter your suggestion: ')
        time.sleep(0.3)
        if not player_number.isnumeric():
            print(f'This is not a whole number!{name}, please enter again!')
            continue
        elif int(player_number) < 0 or int(player_number) > 100:
            print(f'Number must be between 1 and 100 including!{name}, please enter again!')
            continue
        else:
            diff = abs(computer_number - int(player_number))
            if diff == 0:
                time.sleep(0.4)
                print(f'{name}, {player_number} is the secret of computer!')
                game = next_game()
                break
            time.sleep(0.5)
            if diff > 50:
                print('Cold, like the heart of your EX!')
            elif diff > 40:
                print(f'{name}, very cold! Are we in Finland?')
            elif diff > 30:
                print(f'Cold! Not even close!')
            elif diff > 20:
                print('Nice and warm! Like spain in November')
            elif diff > 10:
                print('It, is hot here!')
            elif diff > 5:
                print(f'{name}, here is Very hot!')
            elif diff >= 1:
                print('Almost there! We are melting! Very Very HOT!')
    if game:
        time.sleep(0.8)
        print(f'The computer has a new secret.')
        time.sleep(0.8)
        print(f'This is a whole number between 1 and 100.')
        time.sleep(0.8)
        print(f'{name}, try to guess, the new secret!')
time.sleep(0.8)
print(f'{name}, bye! Come again to play!')
time.sleep(0.8)
print('GAME OVER!')
