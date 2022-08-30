# an exercise on data types in python and conversion
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill?:\n$"))
numPeople = float(input("How many people to split the bill\n"))
tipPercent = float(input("What percentage tip would you like to give?\n"))
print(f"Each person should pay: \n${round(totalBill/numPeople*(100+tipPercent)/100,2)}")
