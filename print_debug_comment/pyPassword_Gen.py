# pyPassword_Gen
import string
import random

print("Welcome to pyPassword Generator!")
pw_len = int(input("How many letters in password?\n"))
pw_sym = int(input("How many symbols in password?\n"))
pw_num = int(input("How many numbers in password?\n"))
newPassword = []
finalPassword = ""
# for the value of each category above, loop and append a random letter,symbol,num to the password accordingly
# jumble up by passing into another for loop, where a letter is chosen from the newPassword list and appended to a finalPassword list,
# the chosen letter will be removed from the original newPassword list and continue using len(newPassword) until it is 0
for i in range(pw_len):
    newPassword += random.choice(string.ascii_letters)
for i in range(pw_sym):
    newPassword += random.choice(string.punctuation)
for i in range(pw_num):
    newPassword += random.choice(string.digits)

for i in range(len(newPassword)):
    currentIndex = random.randint(0, len(newPassword)-1)
    finalPassword += newPassword[currentIndex]
    newPassword.pop(currentIndex)
else:
    print(finalPassword)