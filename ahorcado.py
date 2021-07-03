import random
from os import system

hung_images = ['''
 +---+
 |   |
     |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
 =========''', '''
 
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Enter more words if you wish in lower case letters
words = 'garcia jhon lucas'.split()

def get_random_word(word_list):
    index_words = random.randint(0, len(word_list) - 1)
    return word_list[index_words]

def show_board(hung_images, incorrect_letters, correct_letters, secret_word):
    system("clear")
    print('H A N G E D')
    print(hung_images[len(incorrect_letters)])
    print()

    print('Incorrect lettering:', end = ' ')
    for letter in incorrect_letters:
        print(letter, end = ' ')
    print()

    empty_spaces = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            empty_spaces = empty_spaces[:i] + secret_word[i] + empty_spaces[i+1:]

    for letter in empty_spaces:
        print(letter, end = ' ')

    print()

def get_attempt(tested_letters):
    while True:
        print('Guess the letter')
        attempt = input()
        attempt = attempt.lower()
        print(attempt)
        if len(attempt) != 1:
            print('Please enter a letter')
        elif attempt in tested_letters:
            print('You have already tried this letter Choose another one')
        elif attempt not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Please enter a letter')
        else:
            return attempt

def new_game():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('s')

incorrect_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_finished = False

while True:
    show_board(hung_images, incorrect_letters, correct_letters, secret_word)
    attempt = get_attempt(incorrect_letters + correct_letters)

    if attempt in secret_word:
        correct_letters = correct_letters + attempt
        finding_letters = True

        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                finding_letters = False
                break

        if finding_letters:
            print('Yes! The secret word is "' + secret_word + ' "You have won!')
            game_finished = True 

    else:
        incorrect_letters = incorrect_letters + attempt

        if len(incorrect_letters) == len(hung_images) - 1:
            show_board(hung_images, incorrect_letters, correct_letters, secret_word)
            print("You've run out of attempts! " + str(len(incorrect_letters)) + ' failed attempts and ' + str(len(correct_letters)) + ' hits, the word was "' + secret_word + '"')
            game_finished = True

    if game_finished:
        if new_game():
            incorrect_letters = ''
            correct_letters = ''
            game_finished = False
            secret_word = get_random_word(words)
        else:
            break
