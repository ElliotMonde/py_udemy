# exercise to output the years, months,weeks,days left in a person's life after receiving input of current age
"""
from datetime import datetime
birthDate = [int(input("Which year were you born?\n")), int(input("Which month (numerically) were you born in?\n"))]
currentDate = [int(datetime.today().year), int(datetime.today().month)]
currentAgeInMonths = (currentDate[0]-birthDate[0]) *12+(currentDate[1]-birthDate[1])
lifeLeftMonths = 90*12-currentAgeInMonths
print(f"You are currently {currentDate[0]-birthDate[0]} years, {currentDate[1]-birthDate[1]} months old. If you were to live till 90, you have {int((lifeLeftMonths)/12)} years and {int((lifeLeftMonths)%12)} months left..")

"""
currentAge = int(input("What is your numerical age?\n"))
yearsLeft = 90 - currentAge
print(f"You have {yearsLeft*365} days, {yearsLeft*52} weeks, {yearsLeft*12} months left, if you even live till 90..")