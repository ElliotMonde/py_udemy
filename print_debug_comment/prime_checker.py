# check if input is prime number
# pre-cond: input must be integer >1

# slightly shorter method checking if the user's num is divisible by other primes before it
prime_arr = [1,2]
def find_prime(arr,num):
    # take in a max num
    # start a counter from 2, while lower than the item in array, is it divisible by the array items = [2,3,5,7,..] ?
    # if next item is greater and has not break loop, append num to list
    if num>1:    
        for item in range(2,num+1):
            for primeIndex in range(1,len(arr)):
                if (item%arr[primeIndex]==0):
                    break
                elif (primeIndex == len(arr)-1) and (item%arr[primeIndex] != 0):
                    arr.append(item)
    if (num in arr):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    print(arr) 

# long method dividing by all numbers before the user's num
def prime_check(num):
    if num != 1 or num != 2:
        for item in range(2,num):
            if (num%item == 0):
                return print(f"{num} is not a prime number, it is divisible by {item}.")
    print(f"{num} is a prime number.")       
    
userInp = int(input("Enter a positive integer to check if it's a prime:\n"))
prime_check(userInp)
find_prime(prime_arr,userInp)