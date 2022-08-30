import random
nameList = str.split(input("Input all players' name separated by a comma:\n"),",")
print(f"{nameList[random.randint(0,len(nameList))]} will pay the bills.")