userInput = round(float(input("Input a number:\n")))
if userInput%2 == 0:
    print("This is an even number.")
elif userInput%2 != 0:
    print("This is an odd number.")
else:
    print("invalid input.")
