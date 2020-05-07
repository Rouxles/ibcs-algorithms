def factorial(x):
    if x == 1:
        return 1 # base case
    else:
        return x*factorial(x-1) # recursive case

for x in range(1,11): # can't start from 0
    print(factorial(x))

