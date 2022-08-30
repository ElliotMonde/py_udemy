# highest score
print("To find the highest score,")
list_scores=str.split(input("Input all the scores separated by a comma:\n"),",")
highest=0
for score in list_scores:
    score = float(score)
    if score>highest:
        highest=score
else:
    print(f"Highest score is {highest}")