year_to_check = int(input("Is this a leap year? Input year:\n"))
if (year_to_check%4==0 and (year_to_check%100 != 0 or year_to_check%400 == 0)):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")