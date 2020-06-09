# In this file, we assume that a list created is a queue, where the only operations that can be done would be to push to the end of the list and to popleft

from collections import deque

queue = []

def add_node(for_insert, q):
    queue = q.copy() # Makes a copy of the queue (for mutability purposes)
    queue.append(for_insert) # The name for this would be enqueue, but in python, append has the same effect

def delete_node(q):
    queue = q.copy()
    queue.popleft() # The name for this would be dequeue, but in python, popleft (with the collections module) has the same effect
    # popleft here basically does the same thing as pop, but starts from the left instead (which emulates a queue in python)

def traverse_until_match(to_find, q):
    queue = q.copy()
    while len(queue) != 0: # Checks to see if the queue is empty
        if queue.popleft() == to_find: 
            print(to_find)
    print("not found")


def traverse_whole(q):
    queue = q.copy()
    while len(queue) != 0: 
        print(queue.popleft()) 