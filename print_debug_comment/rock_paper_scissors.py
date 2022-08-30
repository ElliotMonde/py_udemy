import math
from random import randint
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


def game():
    print("ROCK PAPER SCISSORS!!!!")
    userChoice = input("Choose '1' for Rock, '2' for Scissors, '3' for Paper!\n")
    if (userChoice == 'quit'):
        return
    else:
        userChoice = int(userChoice)
    comChoice = randint(1,3)
    choiceArr = ['Rock','Scissors','Paper']
    stdText = f"You chose {choiceArr[userChoice-1]}, Computer chose {choiceArr[comChoice-1]}!!\n"
    match (userChoice-comChoice):
        case 1 | -2:
            print(f"YOU LOSE!!!\n{stdText}\n")
        case -1 | 2:
            print(f"YOU WIN!!!\n{stdText}\n")
        case 0:
            print(f"IT'S A TIE!!!\n{stdText}\n")
        case _: print(stdText)
    game()
game()