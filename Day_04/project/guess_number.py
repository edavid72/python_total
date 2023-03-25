from random import randint
import os
from colorama import init, Fore, Back


def gues_number():
    secret_number = randint(1, 10)
    user_number = 0
    attemps = 8
    success = False

    # Your Name
    name = input(Fore.GREEN + "Hola!, ready to start, well first tell me your name? : ")

    os.system('clear')
    print(f"\nVery good {name}, I just thought of a number between 1 and 10 and your mission is to "
          f"guess it, "
          f"you have {attemps} attemps, let's start")

    while user_number != secret_number and attemps > 0:
        user_number = int(
            input(Fore.LIGHTYELLOW_EX + f'You have {attemps} attempts, what is the number I '
                                        f'thought of ? '))
        attemps -= 1

        if user_number not in range(1, 10):
            print('tu nmero es diferente')
        elif user_number == secret_number:
            os.system('clear')
            print(f'\nCongratulations {name} you have won, you have guessed that the secret number '
                  f'was '
                  f'{secret_number} !!')
            print(f'\nSecret number: {secret_number}')
            print(f'\nNumber of failed attempts: {8 - attemps}')
        elif user_number < secret_number:
            print(f'My number is greater than {user_number}')
        elif user_number > secret_number:
            print(f'My number is less than {user_number}')
        elif attemps == 0:
            os.system('clear')
            print(Fore.RED + f'\nSorry {name} You Lost, the secret number was {secret_number}')


# Run Function
gues_number()
