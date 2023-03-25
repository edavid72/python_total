'''Ahorcado GAME'''
import os
from random import choice

words = ['tiburon', 'motocicleta', 'helipuerto', 'chocolate']
correct_letters = []
wrong_letters = []
attempts = 6
hits = 0
game_over = False


# Function #1: Random Word
def random_word(words_list):
    word = ''

    word = choice(words_list)
    unique_letters = len(set(word))

    return word, unique_letters


selected_word, single_letters = random_word(words)


# Function #2: Hidden Board
def hidden_board(hiden_word):
    hidden_list = []

    for letter in hiden_word:
        if letter in correct_letters:
            hidden_list.append(letter)
        else:
            hidden_list.append('_')

    print(' '.join(hidden_list))


# Function #3: Request Letter
def request_letter():
    user_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        user_letter = input('Enter a letter: ').lower()
        if user_letter in alphabet and len(user_letter) == 1:
            is_valid = True
        else:
            print('You have not entered a correct letter, please try again:')

    return user_letter


# selected_letter = request_letter()


# Function #4: Check letter
def check_user_letter(user_letter, hidden_word, lives, coincidences):
    end = False

    if user_letter in hidden_word and user_letter not in correct_letters:
        correct_letters.append(user_letter)
        coincidences += 1
    elif user_letter in hidden_word and user_letter in correct_letters:
        print(f'You have already found this "{user_letter}" letter, try a different one')
    else:
        wrong_letters.append(user_letter)
        lives -= 1

    if lives == 0:
        end = lose()
        print(end)
    elif coincidences == single_letters:
        end = win(selected_word)
        print(end)

    return end, lives, coincidences


def lose():
    print('You have run out of lives!')
    print(f'The hidden word was: {selected_word}')

    return True


def win(word):
    hidden_board(selected_word)
    print(f'Congratulations you won, you managed to discover the word: {selected_word}')

    return True


while not game_over:
    os.system('clear')
    print('\n' + '*' * 20 + '\n')
    hidden_board(selected_word)
    print('\n')
    print('Wrong letters: ' + '-'.join(wrong_letters))
    print(f'Lives: {attempts}')

    selected_letter = request_letter()
    game_over, attempts, hits = check_user_letter(selected_letter, selected_word, attempts, hits)
