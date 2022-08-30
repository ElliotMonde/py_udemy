# for a list range of [1,101),
# if current item is divisible by 3, output Fizz instead of the number
# if current item is divisible by 5, output Buzz instead of the number
# if current item is divisible by both 3 and 5, output FizzBuzz
print("Welcome to FizzBuzz!")
upper_lim=int(input("What is the max number for this round?\n"))+1
for num in range(1,upper_lim):
    if num%15 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)