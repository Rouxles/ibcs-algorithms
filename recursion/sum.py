def sum(x): # this would kinda be like the functional programming function reduce()
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:]) # x[1:] takes the list and returns from index 1 onwards
    

list = [1,2,3,4,5,6,7,8,9]

print(sum(list))