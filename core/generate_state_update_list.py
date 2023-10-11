from core.synchronous_update import synchronous_update


def find_basin_of_one_state(lst):
    basin = []

    # Find the attractor in the array
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                basin = lst[i:j]
                break
        if len(basin) > 0:
            break

    # Print the cycle
    if basin:
        return True
    else:
        return False


def generate_state_update_list(initial_stat, boolean_function, k):
    state_update_lst = [initial_stat]
    temp = initial_stat

    while True:
        update = synchronous_update(temp, boolean_function, k)
        temp = update
        state_update_lst.append(update)

        found = find_basin_of_one_state(state_update_lst)

        if found:
            return state_update_lst

# print(generate_state_update_list([0, 0, 1, 0], [[[1,1,2,4], [1,0,0,0], [1,0,0,1], [1,0,1,0], [0,0,1,1], [0,1,0,0],
# [0,1,0,1], [1,1,1,0], [1,1,1,1]], [[2,1,2,3], [0,0,0,0], [0,0,0,1], [1,0,1,0], [0,0,1,1], [0,1,0,0], [0,1,0,1], [1,
# 1,1,0], [1,1,1,1]], [[3,1,3,4], [1,0,0,0], [1,0,0,1], [0,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [0,1,
# 1,1]], [[4,1,3,4], [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [0,1,1,1]]], 3 ))
