import os
import csv
from random import randint
import msvcrt as m
import re


def clear():
    _ = os.system('cls')


def print_movie_guessed(movie_guessed):
    for i in range(0,len(movie_guessed)):
        print(movie_guessed[i], end = "")


def load_movie_list(industry, file_name):
    movie_list = []
    with open(file_name) as data_file:
        data = csv.reader(data_file, delimiter = ',')
        next(data)
        for row in data:
            movie_list.append(row[0])
    return movie_list


def pick_random_movie(movie_list):
    movie_index = randint(0, len(movie_list))
    return movie_list[movie_index]


def replace_letter(letter_guessed, movie_guessed, movie_name):
    for i in range(0, len(movie_guessed)):
        if(letter_guessed == movie_name[i]):
            movie_guessed[i] = letter_guessed
    return movie_guessed


def print_hangman(count):

    if count == 1:
        hangman_pattern[2] = ' //          O'
    elif(count == 2):
        hangman_pattern[3] = ' ||          |'
        hangman_pattern[4] = ' ||          |'
    elif(count == 3):
        hangman_pattern[3] = ' ||         \\|'
    elif(count == 4):
        hangman_pattern[3] = ' ||         \\|/'
    elif(count == 5):
        hangman_pattern[5] = ' ||         / '
    elif(count == 6):
        hangman_pattern[5] = ' ||         / \\'

    for i in hangman_pattern:
        print(i)
    print('\n\n\n\n\n')

def print_game_title():
    print('\n\n')
    print(' ##################################################################################################')
    print(' ##################################################################################################')
    print('           ##    ##      ####      ###   ##   #######   ###   ###      ####      ###   ##')
    print('           ##    ##     ##  ##     ####  ##   ##        #### ####     ##  ##     ####  ##')
    print('           ########    ########    ## ## ##   ##  ###   ## ### ##    ########    ## ## ##')
    print('           ##    ##   ##      ##   ##  ####   ##   ##   ##     ##   ##      ##   ##  ####')
    print('           ##    ##  ##        ##  ##   ###   #######   ##     ##  ##        ##  ##   ###')
    print(' ##################################################################################################')
    print(' ##################################################################################################')
    print('\n\n\n\n\n')

#########################################################################################################
#########################################################################################################

while(True):

    hangman_pattern = list()
    hangman_pattern.append('    ==========')
    hangman_pattern.append('  //        ||')
    hangman_pattern.append(' //')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append(' ||')
    hangman_pattern.append('=================')

    exit_char = '1'
    if(exit_char == '2'):
        break
    clear()
    while(True):
        print_game_title()
        industry = input('Hollywood / Bollywood?\n1.Hollywood\n2.Bollywood\n\nType 1 or 2: ')
        clear()
        print_game_title()
        if(industry == '1'):
            file_name = 'Hollywood.csv'
            break
        elif(industry == '2'):
            file_name = 'Bollywood.csv'
            break
        elif(industry == 'All'):
            file_name = ''
        else:
            print('Invalid Choice!')
    movie_guessed = []
    movie_list = load_movie_list(industry, file_name)
    movie_name = pick_random_movie(movie_list)
    movie_name = movie_name.upper()
    movie_name_length = len(movie_name)

    for i in range(0, movie_name_length):
        if(bool(re.match('[\s\.\-\'\"\`\~\_\=]',movie_name[i]))):
            movie_guessed.append(movie_name[i])
        else:
            movie_guessed.append('-')

    #print(movie_name)


    guesses = []
    movie_letters = []
    for letter in movie_name:
        if(letter == ' '):
            continue
        elif(letter in movie_letters):
            continue
        else:
            movie_letters.append(letter)

    first_guess = True

    #print(movie_letters)

    count = 0

    print_hangman(count)
    print_movie_guessed(movie_guessed)
    print('\n\n')

    break_check = False
    while(count<6):
        break_check = False
        for i in range(0, len(movie_name)):
            if(movie_name[i] == movie_guessed[i]):
                if(i == (len(movie_name)-1)):
                    break_check = True
            else:
                break
        if(break_check):
            break
        letter_guessed = input('Guess a Letter/Number: ')

        if(len(letter_guessed) == 1):
            if(bool(re.match('[a-zA-Z0-9]', letter_guessed))):
                if(bool(re.match('[a-z]', letter_guessed))):
                    letter_guessed = letter_guessed.upper()

            if(len(guesses) == 0):
                guesses.append(letter_guessed)
                if(letter_guessed not in movie_letters):
                    count = count+1
                elif(letter_guessed in movie_letters):
                    movie_guessed = replace_letter(letter_guessed, movie_guessed, movie_name)
                clear()
                print_game_title()

            else:
                if(letter_guessed not in guesses):
                    guesses.append(letter_guessed)
                    if(letter_guessed not in movie_letters):
                        count = count+1
                    elif(letter_guessed in movie_letters):
                        movie_guessed = replace_letter(letter_guessed, movie_guessed, movie_name)
                    clear()
                    print_game_title()
                else:
                    clear()
                    print_game_title()
                    print('\n\n\t\tCharacter already guesses before!\n\n')


            print_hangman(count)
            print_movie_guessed(movie_guessed)
            print('\n\nGuessed Characters: ',guesses)

        else:
            clear()
            print_game_title()
            print('\n\n\n\n\n\t\tEnter a valid character! (A-Z, 0-9)\n\n\n')
            print_hangman(count)
            print_movie_guessed(movie_guessed,'\n\n')


    if(count == 6):
        print('\n\n\nOops! You\'re out of chances!')
        print('MOVIE NAME WAS: ', movie_name)
    else:
        print('\n\n\nHurray!\nYou won!')
    exit_char = input('\n\n1. Play another round\n2. Quit\nChoose: ')
    if(exit_char == '2'):
        break
