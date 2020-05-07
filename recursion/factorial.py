def factorial(x):
    if x == 1:
        return 1 # base case
    else:
        return x*factorial(x-1) # recursive case

for x in range(1,11): # can't start from 0
    print(factorial(x))

'''
The way recursion works in python is essentially this:
Each extra recursion creates a new stack, and after it reaches the base case, it then unwinds back to return the answer

Example is like the following (factorial 4)

factorial(4)
return 4 * factorial(4-1)
    return 3 * factorial(3-1)
        return 2 * factorial(2-1)
            return 1

And then, factorial(2-1) will return 1, which will then be plugged into return 2 * 1, and the value of that will then be equal to factorial(3-1) and on and on and on
'''

'''
If you need an extra visualization of what's going on behind the scenes as python executes the program, plug in this code into the link below
http://www.pythontutor.com/visualize.html#mode=display
'''