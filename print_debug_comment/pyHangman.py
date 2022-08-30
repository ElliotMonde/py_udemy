# pyHangman
# body parts functions: top with/out head, mid with/out body, bot with/out legs, base
# generate random word, get length, array for full word using list, array for empty array of '_' blanks using len
# function to get input and check if letter exist, replace all blank spaces that matches the index by cross checking the word array.
# print out the current blank array before the next input
#put all in main function, function to output blanks array, function to print out hangman portions, call own main function
# the body parts functions are in a list, the number of wrong guesses are tracked in a state variable. use a for loop to output the body parts in array using range(0,wrong_state)
# if wrong_state == len(body_arr)-1, call gameover function.
from random_word import RandomWords

top = "\n    -----------------\n    |              ||\n    |              ||"
midOne = "\n    |              ||"
midTwo ="\n                   ||"
bot="\n-------------------||---------"
head="\n   (_)             ||"
body="\n    |              ||"
right_arm="\n   /|              ||"
both_arms="\n   /|\             ||"
right_leg="\n   /               ||"
both_legs="\n   / \             ||"

stage_one = [top, midOne, midOne, midTwo, midTwo, midTwo, midTwo, midTwo, bot]
stage_two = [top, midOne, midOne, head, midTwo, midTwo, midTwo, midTwo, bot]
stage_three = [top, midOne, midOne, head, body, midTwo, midTwo, midTwo, bot]
stage_four = [top, midOne, midOne, head, right_arm, midTwo, midTwo, midTwo, bot]
stage_five = [top, midOne, midOne, head, both_arms, midTwo, midTwo, midTwo, bot]
stage_six = [top, midOne, midOne, head, both_arms, right_leg, midTwo, midTwo, bot]
stage_seven = [top, midOne, midOne, head, both_arms, both_legs, midTwo, midTwo, bot]
hangman_arr = [stage_one,stage_two,stage_three,stage_four,stage_five,stage_six,stage_seven]

print("Welcome to pyHangman!")
r = RandomWords()
get_word = r.get_random_word(hasDictionaryDef="true")
new_word = list(get_word)
blank_arr = len(new_word)*["_"]
wrong_state = 0

def check(letter,wrong_state):
    correct=0
    for index,elem in enumerate(new_word):
        if elem == letter:
            if correct == 0:
                correct = 1
            blank_arr[index] = letter
    if correct == 0:
        wrong_state+=1
    return wrong_state
def win():
    for item in blank_arr:
        if item == "_":
            return "false"
    return "true"
def guess(wrong_state):
    print(wrong_state)
    for item in hangman_arr[wrong_state]:
        print(item)
    print(blank_arr)
    current_letter = input("Guess a letter: ")
    wrong_state=check(current_letter,wrong_state)
    if wrong_state == len(hangman_arr)-1:
        print("GAME-OVER! XP")
        print(f"The word is {str(new_word)}")
    elif win() == "true":
        print("Congratulations! You Win!")
        print(f"The word is {str(new_word)}")
    else:
        guess(wrong_state)

guess(wrong_state)
