"""
guess the number the com is thinking off (1 ~ 100)
pre-cond: number chosen is an integer >0 and <=100
easy-mode: 25 tries, medium-mode: 10 tries, hard-mode: 5 tries
"""

from random import randint, random, seed

def choose_difficulty():
    match(str.lower(input("Choose difficulty: easy | med | hard: "))):
        case 'easy':
            return 25
        case 'med':
            return 10
        case 'hard':
            return 5
        case _ :
            print("invalid difficulty settings, pls restart game.")
            return choose_difficulty()

def start_game():
    tries = choose_difficulty()
    seed()
    chosen_num = randint(1,100)
    usr_guess = None
    while tries > 0 and usr_guess != chosen_num:
        usr_guess = int(input("Guess the number the computer is thinking of: "))
        if usr_guess > chosen_num:
            print("Guess is too high!")
        elif usr_guess < chosen_num:
            print("Guess is too low!")
        tries -= 1

    print("You guessed it!") if usr_guess == chosen_num else print("Too bad! Ran out of tries!")
    if str.upper(input("Play again? [Y/N]: ")) == 'Y':
        return start_game()

start_game()