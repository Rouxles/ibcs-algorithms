# In this file, we assume that a list created is a stack, where the only operations that can be done would be to push to the end of the list and to pop from the end of the list.

stack = [1,2,3,4,5,6,7,8]

def add_to_stack(for_insert, s):
    stack = s.copy() # Makes a copy of the stack (for mutability purposes)
    stack.append(for_insert)

def remove_from_stack(s):
    stack = s.copy()
    stack.pop()

def traverse_until_match(to_find, s):
    stack = s.copy()
    while len(stack) != 0:
        if stack.pop() == to_find:
            print(to_find)
    print("not found")


def traverse_whole_list(s):
    stack = s.copy()
    while len(stack) != 0: # Checks to see if the stack is empty
        print(stack.pop())