from synchronous_update import synchronous_update
import numpy as np

def find_attractor(lst):
    pattern = []

    # Find the pattern in the array
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                pattern = lst[i:j]
                break
        if len(pattern) > 0:
            break

    # Find the cycle containing the pattern
    cycle = []
    for i in range(len(lst)):
        if lst[i:i+len(pattern)] == pattern:
            cycle = lst[i:i+len(pattern)*(i>0)]
            break

    # Return the cycle
    if cycle:
        return True, cycle
    else:
        return False, []

def update_list(initial_stat, boolean_function, k):
    state_trans_lst = []
    temp = initial_stat
    found = False

    while True:
        update = synchronous_update(temp, boolean_function, k)
#        print(update)
        temp = update
        state_trans_lst.append(update)
        print(state_trans_lst)

        found, cycle = find_attractor(state_trans_lst)

        if found:
            return cycle
            break

update_list([1,0,1], [[[1, 2, 3], [1, 1, 1], [0, 1, 0], [0, 0, 1], [1, 0, 0]],
                      [[2, 2, 3], [1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 0, 0]],
                      [[3, 1, 2], [0, 1, 1], [0, 1, 0], [1, 0, 1], [0, 0, 0]]], 2)