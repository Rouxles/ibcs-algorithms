def fibonacci(x):
    if x == 0 or x == 1:
        return x 
    else:
        return fibonacci(x-1) + (fibonacci(x-2))

for x in range(11):
    print(fibonacci(x))