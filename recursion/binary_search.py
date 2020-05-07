list_one = sorted([621,420,69,42069,321,94,267])
list_two = sorted([621,420,69,42069,321,94,267,846])

def binary_search(x, target, upper, lower=0):
    mid = (upper + lower)//2
    if target == x[mid]:
        return mid # this is the index value
    if x[mid] < target:
        return binary_search(x, target, upper, mid+1) # doesn't need to start from mid as it has already checked it
    if x[mid] > target:
        return binary_search(x, target, mid-1, lower)
    return False
    

def maximum_index(x):
    return len(x)-1

target = 621 # let target for both be 621 for simplicity sake - you can change this manually to suit your needs, and also add a presence check if need be

index = binary_search(list_one, target, maximum_index(list_one)) # change the list to odd or even to check whether it works for both cases or not

if index:
    print("Value found at index {}".format(index))
else:
    print("Value not found in index")
