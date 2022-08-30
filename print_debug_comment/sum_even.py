# add all even numbers in an input list
# get list input, str.split input
# loop through list items, if item%2 == 0, add to final total, print final total
print("To add all even numbers,")
list_num=str.split(input("Input all numbers here, separated by a comma:\n"),",")
total = 0
for num in list_num:
    num = int(num)
    if num%2==0:
        total+=num
print(f"sum of all even numbers in the list:\n{total}")