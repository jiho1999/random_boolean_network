from synchronous_update import synchronous_update
import numpy as np

def find_attractor(lst):
    attractor = []

    # Find the attractor in the array
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                attractor = lst[i:j]
                break
        if len(attractor) > 0:
            break

    # Print the cycle
    if attractor:
        return True
    else:
        return False

def update_list(initial_stat, boolean_function, k):
    state_trans_lst = []
    state_trans_lst.append(initial_stat)
    temp = initial_stat

    while True:
        update = synchronous_update(temp, boolean_function, k)
        temp = update
        state_trans_lst.append(update)

        found = find_attractor(state_trans_lst)

        if found:
            return state_trans_lst
