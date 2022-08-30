import string


alphabet = list(string.ascii_letters)


def input_text():
    inputText = input("Input text:\n")
    inputShift = int(input("Input shift number:\n"))
    return inputText, inputShift

def encrypt(alphabet):
    hold = []
    [plaintext, shift_num] = input_text()
    for index, letter in enumerate(plaintext):
        for num,item in enumerate(alphabet):
            if plaintext[index] == alphabet[num]:
                num = num+shift_num
                if num>52:
                    num=num%52
                hold.append(alphabet[num])
                break
            elif plaintext[index] == ' ':
                hold.append(' ')
                break
    hold_str = ''
    for i in hold:
        hold_str += i
    print(hold_str)

def decrypt(alphabet):
    hold = []
    [ciphertext, shift_num] = input_text()
    for index, letter in enumerate(ciphertext):
        for num, item in enumerate(alphabet):
            if ciphertext[index] == alphabet[num]:
                num = num - shift_num
                while num < 0:
                    num=num%52
                hold.append(alphabet[num])
                break
            elif ciphertext[index] == ' ':
                hold.append(' ')
                break
    hold_str = ''
    for i in hold:
        hold_str+= i
    print(hold_str)

print("Welcome to Caesar Cipyher")
choice = input("To encrypt, type 'encrypt'. To decrypt type 'decrypt':\n")
if choice == 'encrypt':
    encrypt(alphabet)
elif choice == 'decrypt':
    decrypt(alphabet)

"""
# input encrypt or decrypt
# ask for plaintext to encrypt or ciphertext to decrypt
# ask for shift number to encrypt, ask for shift number to decrypt
# output plaintext or ciphertext
# ask if user wish to output was satisfactory or retry

def input_text():
    inputText = bytes(input("Input text:\n"),"utf-8")
    inputShift = int(input("Input shift number:\n"))
    return inputText,inputShift

def encrypt():
    hold = []
    [plaintext,shift_num]=input_text()
    for index,letter in enumerate(plaintext):
        changed_letter = plaintext[index]+shift_num

        hold.append(changed_letter)
    out_str = bytes(hold)
    print(out_str)

def decrypt():
    hold = []
    [ciphertext,shift_num]=input_text()
    for index,letter in enumerate(ciphertext):
        changed_letter = ciphertext[index]-shift_num
        hold.append(changed_letter)
    out_str = bytes(hold)
    print(out_str)
"""
