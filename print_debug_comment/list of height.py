# list of height

print("To find the average height,")
list_height = str.split(input("Input all the heights separated by comma:\n"),",")
total_height= 0
for height in list_height:
    total_height+= round(float(height))
else:
    print(f"Average height is {round(total_height/len(list_height),2)}.")